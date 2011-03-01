%include	/usr/lib/rpm/macros.php
%define		_class		HTML
%define		_subclass	Form
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - simple HTML form package
Summary(pl.UTF-8):	%{_pearname} - pakiet do prostych formularzy HTML
Name:		php-pear-%{_pearname}
Version:	1.3.0
Release:	3
Epoch:		0
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	5dac87216afa9f388bd55cb546d5413c
URL:		http://pear.php.net/package/HTML_Form/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-common >= 3:4.0.0
Requires:	php-pear
Obsoletes:	php-pear-HTML_Form-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a simple HTML form generator. It supports all the HTML form
element types including file uploads, may return or print the form,
just individual form elements or the full form in "table mode" with a
fixed layout.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
To jest generator prostych formularzy HTML. Obsługuje wszystkie typy
elementów formularzy HTML włącznie z przesyłaniem plików; może zwrócić
lub wypisać formularz, same elementy formularza lub pełny formularz w
"trybie tabeli" z ustalonym rozmieszczeniem.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
