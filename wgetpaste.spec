Summary:	Paste to Paste sites from terminal
Name:		wgetpaste
Version:	2.18
Release:	1
License:	GPL v2+
Source0:	http://wgetpaste.zlin.dk/%{name}-%{version}.tar.bz2
# Source0-md5:	0085d679445af9e6f695d036abee106d
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

%prep
%setup -q
%{__sed} -i -e '1s,^#!.*bash,#!/bin/bash,' %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -Dp %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/wgetpaste
