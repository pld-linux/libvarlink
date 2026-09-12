Summary:	C implementation of the varlink protocol and command line tool
Summary(pl.UTF-8):	Implementacja w C protokołu varlink oraz narzędzia linii poleceń
Name:		libvarlink
Version:	24.0.1
Release:	1
License:	Apache v2.0
Group:		Libraries
#Source0Download: https://github.com/varlink/libvarlink/releases
Source0:	https://github.com/varlink/libvarlink/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	d99e57983dfe63b30817fdb61bd1f7c6
URL:		https://varlink.org/
BuildRequires:	gcc >= 5:3.2
BuildRequires:	meson >= 0.40
BuildRequires:	ninja >= 1.5
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
varlink is an interface description format and protocol that aims to
make services accessible to both humans and machines in the simplest
feasible way.

A varlink interface combines the classic UNIX command line options,
STDIN/OUT/ERROR text formats, man pages, service metadata and provides
the equivalent over a single file descriptor, a.k.a. "FD3".

varlink is plain-text, type-safe, discoverable, self-documenting,
remotable, testable, easy to debug. varlink is accessible from any
programming environment.

This package provides varlink C library and command line tool.

%description -l pl.UTF-8
varlink to format opisu interfejsu oraz protokół, którego celem jest
udostępnienie usług zarówno ludziom, jak i maszynom w możliwie
najprostszy sposób.

Interfejs varlink łączy klasyczne opcje uniksowej linii poleceń,
formaty tekstowe standardowego wejścia/wyjścia/diagnostyki, strony
podręcznika man, metadane usług oraz udostępnia odpowiednik poprzez
pojedynczy deskryptor pliku, czyli "FD3".

varlink to protokół tekstowy, bezpieczny pod kątem typów, pozwalający
na wykrywanie usług, samodokumentujący się, zdalny, testowalny, łatwo
diagnozowalny. Jest dostępny z dowolnego środowiska programistycznego.

Ten pakiet zawiera bibliotekę C varlink oraz narzędzie linii poleceń.

%package devel
Summary:	Header files for libvarlink library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libvarlink
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libvarlink library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libvarlink.

%package -n bash-completion-varlink
Summary:	bash-completion for varlink
Summary(pl.UTF-8):	Bashowe dopełnianie parametrów polecenia varlink
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	bash-completion >= 1:2.0
BuildArch:	noarch

%description -n bash-completion-varlink
bash-completion for varlink.

%description -n bash-completion-varlink -l pl.UTF-8
Bashowe dopełnianie parametrów polecenia varlink.

%package -n vim-plugin-varlink
Summary:	varlink integration for Vim
Summary(pl.UTF-8):	Integracja varlink dla Vima
Group:		Applications/Editors/Vim
Requires:	vim-rt
BuildArch:	noarch

%description -n vim-plugin-varlink
varlink integration for Vim.

%description -n vim-plugin-varlink -l pl.UTF-8
Integracja varlink dla Vima.

%prep
%setup -q

%build
%meson

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md README.md
%attr(755,root,root) %{_bindir}/varlink
%{_libdir}/libvarlink.so.0

%files devel
%defattr(644,root,root,755)
%{_libdir}/libvarlink.so
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
