# TODO
# - package zsh completion: _wgetpaste
Summary:	A Script that automates pasting to a number of pastebin services
Summary(pl.UTF-8):	Skrypt który automatyzuje wklejanie do wielu serwisów pastebin
Name:		wgetpaste
Version:	2.22
Release:	1
License:	GPL v2+
Source0:	http://wgetpaste.zlin.dk/%{name}-%{version}.tar.bz2
# Source0-md5:	413e9faf02b044d56ce454fcd90cecbf
Source1:	http://wgetpaste.zlin.dk/%{name}.example
# Source1-md5:	77392c788659cc648a59df2d239ebe19
Group:		Applications/Networking
URL:		http://wgetpaste.zlin.dk/
BuildRequires:	sed >= 4.0
Requires:	coreutils
Requires:	sed
Requires:	wget
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Script that automates pasting to a number of pastebin services
relying only on bash, sed, coreutils (mktemp/sort/tr/wc/whoami/tee)
and wget.

%description(pl.UTF-8):
Skrypt który automatyzuje wklejanie do wielu serwisów pastebin
operając się tylko na bash, sed, coreutils (mktemp/sort/tr/wc/whoami/
tee) i wget.

%prep
%setup -q
%{__sed} -i -e '1s,^#!.*bash,#!/bin/bash,' %{name}
cp -a %{SOURCE1} .

%install
rm -rf $RPM_BUILD_ROOT
install -Dp %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc wgetpaste.example
%attr(755,root,root) %{_bindir}/wgetpaste
