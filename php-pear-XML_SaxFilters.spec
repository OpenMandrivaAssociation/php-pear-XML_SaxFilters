%define		_class		XML
%define		_subclass	SaxFilters
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	0.3.0
Release:	%mkrel 12
Summary:	A framework for building XML filters using the SAX API
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/XML_SaxFilters/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tar.bz2
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
XML_SaxFilters provides a foundation for using Sax filters in PHP. The
original code base was developed by Luis Argerich and published at
http://phpxmlclasses.sourceforge.net/show_doc.php?class=class_sax_filters.html.
Luis discussed how SaxFilters work, using the Sourceforge classes as
an example, in Chapter 10 of Wrox "PHP 4 XML". Luis kindly gave
permission to modify the code and license for inclusion in PEAR.

This version of the Sax Filters makes significant changes to Luis's
original code (backwards compatibility is definately broken),
seperating abstract classes from interfaces, providing interfaces for
data readers and writers and providing methods to help parse XML
documents recursively with filters (for example
AbstractFilter::setParent()) for documents where the structure can
vary significantly.

Sax Filtering is an approach to making parsing XML documents with Sax
modular and easy to maintain. The parser delegates events to a child
filter which may in turn delegate events to another filter. In general
it's possible to implement filters for a document which are as
flexible and powerful as DOM.


%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install
rm -rf %{buildroot}

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean
rm -rf %{buildroot}

%post
%if %mdkversion < 201000
pear install --nodeps --soft --force --register-only \
    %{_datadir}/pear/packages/%{upstream_name}.xml >/dev/null || :
%endif

%preun
%if %mdkversion < 201000
if [ "$1" -eq "0" ]; then
    pear uninstall --nodeps --ignore-errors --register-only \
        %{pear_name} >/dev/null || :
fi
%endif

%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/docs/*
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


