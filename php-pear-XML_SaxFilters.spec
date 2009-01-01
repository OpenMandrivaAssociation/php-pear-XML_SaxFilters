%define		_class		XML
%define		_subclass	SaxFilters
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - a framework for building XML filters using the SAX API
Name:		php-pear-%{_pearname}
Version:	0.3.0
Release:	%mkrel 9
License:	PHP License
Group:		Development/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tar.bz2
URL:		http://pear.php.net/package/XML_SaxFilters/
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	dos2unix
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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

In PEAR status of this package is: %{_status}.

%prep

%setup -q -c

find . -type d -perm 0700 -exec chmod 755 {} \;
find . -type f -perm 0555 -exec chmod 755 {} \;
find . -type f -perm 0444 -exec chmod 644 {} \;

for i in `find . -type d -name CVS` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
    if [ -e "$i" ]; then rm -rf $i; fi >&/dev/null
done

# strip away annoying ^M
find -type f | grep -v ".gif" | grep -v ".png" | grep -v ".jpg" | xargs dos2unix -U

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}/IO

install %{_pearname}-%{version}/*.php %{buildroot}%{_datadir}/pear/%{_class}
install %{_pearname}-%{version}/%{_subclass}/*.php %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}
install %{_pearname}-%{version}/%{_subclass}/IO/*.php %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}/IO

install -d %{buildroot}%{_datadir}/pear/packages
install -m0644 package.xml %{buildroot}%{_datadir}/pear/packages/%{_pearname}.xml

%post
if [ "$1" = "1" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear install --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi
if [ "$1" = "2" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear upgrade -f --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi

%preun
if [ "$1" = 0 ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear uninstall --nodeps -r %{_pearname}
	fi
fi

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/docs/*
%{_datadir}/pear/%{_class}/*.php
%{_datadir}/pear/%{_class}/%{_subclass}
%{_datadir}/pear/packages/%{_pearname}.xml


