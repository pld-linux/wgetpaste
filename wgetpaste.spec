Summary:	Script that automates pasting to a number of pastebin services
Summary(pl.UTF-8):	Skrypt automatyzujący wklejanie do wielu serwisów pastebin
Name:		wgetpaste
Version:	2.30
Release:	1
License:	GPL v2+
Group:		Applications/Networking
Source0:	http://wgetpaste.zlin.dk/%{name}-%{version}.tar.bz2
# Source0-md5:	d6ef00b6e51cdb4a82b9e2e011e2c46c
Source1:	http://wgetpaste.zlin.dk/%{name}.example
# Source1-md5:	77392c788659cc648a59df2d239ebe19
URL:		http://wgetpaste.zlin.dk/
BuildRequires:	rpmbuild(macros) >= 1.719
BuildRequires:	sed >= 4.0
Requires:	coreutils
Requires:	sed
Requires:	wget
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A script that automates pasting to a number of pastebin services
relying only on bash, sed, coreutils (mktemp/sort/tr/wc/whoami/tee)
and wget.

%description -l pl.UTF-8
Skrypt, który automatyzuje wklejanie do wielu serwisów pastebin,
wykorzystując tylko programy bash, sed, coreutils
(mktemp/sort/tr/wc/whoami/tee) i wget.

%package -n zsh-completion-wgetpaste
Summary:	ZSH completion for wgetpaste command
Summary(pl.UTF-8):	Dopełnianie parametrów w ZSH dla polecenia wgetpaste
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	zsh

%description -n zsh-completion-wgetpaste
ZSH completion for wgetpaste command.

%description -n zsh-completion-wgetpaste -l pl.UTF-8
Dopełnianie parametrów w ZSH dla polecenia wgetpaste.

%prep
%setup -q
%{__sed} -i -e '1s,^#!.*bash,#!/bin/bash,' %{name}
cp -a %{SOURCE1} .

%install
rm -rf $RPM_BUILD_ROOT

install -Dp %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -Dp _wgetpaste $RPM_BUILD_ROOT%{zsh_compdir}/_wgetpaste

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc wgetpaste.example
%attr(755,root,root) %{_bindir}/wgetpaste

%files -n zsh-completion-wgetpaste
%defattr(644,root,root,755)
%{zsh_compdir}/_wgetpaste
