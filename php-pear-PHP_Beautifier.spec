%include	/usr/lib/rpm/macros.php
%define         _class          PHP
%define         _subclass       Beautifier
%define		_status		devel
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - beautifier for PHP
Summary(pl):	%{_pearname} - upiêkszacz dla PHP
Name:		php-pear-%{_pearname}
Version:	0.0.7
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	91e747f234c67a6b82748258e148c12d
URL:		http://pear.php.net/package/PHP_Beautifier/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear >= 3:5.0.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program reformat and beautify PHP source code files
automatically.

In PEAR status of this package is: %{_status}.

%description -l pl
Ten program automatycznie przeformatuje i upiêkszy kod ¼ród³owy
aplikacji napisanych w PHP.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%build
cd %{_pearname}-%{version}/scripts
sed 's,"@php_bin@",/usr/bin/php,' php_beautifier > a
mv -f a php_beautifier

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{php_pear_dir}/%{_class}/%{_subclass}/{Batch,Filter}}

install %{_pearname}-%{version}/scripts/php_beautifier $RPM_BUILD_ROOT%{_bindir}
install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/%{_subclass}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}
install %{_pearname}-%{version}/%{_subclass}/Batch/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Batch
install %{_pearname}-%{version}/%{_subclass}/Filter/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Filter

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/{examples,licenses,tests}
%attr(755,root,root) %{_bindir}/php_beautifier
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
