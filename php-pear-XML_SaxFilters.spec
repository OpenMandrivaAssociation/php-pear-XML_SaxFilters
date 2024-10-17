%define		_class		XML
%define		_subclass	SaxFilters
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	0.3.0
Release:	16
Summary:	A framework for building XML filters using the SAX API
License:	PHP License
Group:		Development/PHP
URL:		https://pear.php.net/package/XML_SaxFilters/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tar.bz2
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

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

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/docs/*
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml




%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 0.3.0-14mdv2012.0
+ Revision: 742310
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 0.3.0-13
+ Revision: 679611
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3.0-12mdv2011.0
+ Revision: 613797
- the mass rebuild of 2010.1 packages

* Wed Nov 11 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.3.0-11mdv2010.1
+ Revision: 464962
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.3.0-10mdv2010.0
+ Revision: 441764
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 0.3.0-9mdv2009.1
+ Revision: 322983
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 0.3.0-8mdv2009.0
+ Revision: 237169
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 0.3.0-7mdv2007.0
+ Revision: 82919
- Import php-pear-XML_SaxFilters

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 0.3.0-7mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 0.3.0-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 0.3.0-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 0.3.0-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 0.3.0-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 0.3.0-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 0.3.0-1mdk
- initial Mandriva package (PLD import)

