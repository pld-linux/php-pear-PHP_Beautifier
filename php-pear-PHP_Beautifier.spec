%include	/usr/lib/rpm/macros.php
%define		_class		PHP
%define		_subclass	Beautifier
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - beautifier for PHP
Summary(pl):	%{_pearname} - upi�kszacz dla PHP
Name:		php-pear-%{_pearname}
Version:	0.1.4
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	0d51b0036e6f61df1e80fd1335a41308
Patch0:		%{name}-path_fix.patch
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
Ten program automatycznie przeformatuje i upi�kszy kod �r�d�owy
aplikacji napisanych w PHP.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c
cd %{_pearname}-%{version}
%patch0 -p2

%build
cd %{_pearname}-%{version}/scripts
sed -i -e 's,"@php_bin@",/usr/bin/php,' php_beautifier

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{php_pear_dir}/%{_class}/%{_subclass}/{Batch/Output,Filter,StreamWrapper}}

install %{_pearname}-%{version}/scripts/php_beautifier $RPM_BUILD_ROOT%{_bindir}
install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/%{_subclass}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}
install %{_pearname}-%{version}/%{_subclass}/Batch/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Batch
install %{_pearname}-%{version}/%{_subclass}/Batch/Output/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Batch/Output
install %{_pearname}-%{version}/%{_subclass}/Filter/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Filter
install %{_pearname}-%{version}/%{_subclass}/StreamWrapper/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/StreamWrapper

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/{examples,licenses,tests}
%attr(755,root,root) %{_bindir}/php_beautifier
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
