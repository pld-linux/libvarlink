Summary:	C implementation of the varlink protocol and command line tool
Name:		libvarlink
Version:	23
Release:	1
License:	Apache v2.0
Group:		Libraries
Source0:	https://github.com/varlink/libvarlink/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	f5fb14310ba55a67c1927cef41e759ad
URL:		http://varlink.org
BuildRequires:	meson >= 0.40
BuildRequires:	ninja
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
varlink is an interface description format and protocol that aims to
make services accessible to both humans and machines in the simplest
feasible way.

A varlink interface combines the classic UNIX command line options,
STDIN/OUT/ERROR text formats, man pages, service metadata and provides
the equivalent over a single file descriptor, a.k.a. “FD3”.

varlink is plain-text, type-safe, discoverable, self-documenting,
remotable, testable, easy to debug. varlink is accessible from any
programming environment.

This package provides varlink C library and command line tool.

%package devel
Summary:	Header files for libvarlink library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libvarlink library.

%package -n bash-completion-varlink
Summary:	bash-completion for varlink
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	bash-completion >= 1:2.0
BuildArch:	noarch

%description -n bash-completion-varlink
bash-completion for varlink.

%package -n vim-plugin-varlink
Summary:	varlink integration for Vim
Group:		Applications/Editors/Vim
Requires:	vim-rt
BuildArch:	noarch

%description -n vim-plugin-varlink
varlink integration for Vim.

%prep
%setup -q

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/varlink
%attr(755,root,root) %{_libdir}/libvarlink.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvarlink.so
%{_includedir}/varlink.h
%{_pkgconfigdir}/libvarlink.pc

%files -n bash-completion-varlink
%defattr(644,root,root,755)
%{bash_compdir}/varlink

%files -n vim-plugin-varlink
%defattr(644,root,root,755)
%{_datadir}/vim/vimfiles/after/ftdetect/varlink.vim
%{_datadir}/vim/vimfiles/after/ftplugin/varlink.vim
%{_datadir}/vim/vimfiles/after/syntax/varlink.vim
