%include	/usr/lib/rpm/macros.php
%define		_class		HTML
%define		_subclass	Form
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - Simple HTML form package
Summary(pl):	%{_pearname} - pakiet do prostych formularzy HTML
Name:		php-pear-%{_pearname}
Version:	1.0.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
# Source0-md5:	35c0af3a8b555bdc59b77a04e3b25cc6
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/package/%{_pearname}/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a simple HTML form generator. It supports all the HTML form
element types including file uploads, may return or print the form,
just individual form elements or the full form in "table mode" with a
fixed layout.

This class has in PEAR status: %{_status}.

%description -l pl
To jest generator prostych formalarzy HTML. Obs³uguje wszystkie typy
elementów formularzy HTML w³±cznie z przesy³aniem plików; mo¿e zwróciæ
lub wypisaæ formularz, same elementy formularza lub pe³ny formularz w
"trybie tabeli" z ustalonym rozmieszczeniem.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/%{_class}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{_class}/*.php
