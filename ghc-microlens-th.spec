# generated by cabal-rpm-0.12.1
# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name microlens-th
%global pkgver %{pkg_name}-%{version}

Name:           ghc-%{pkg_name}
Version:        0.4.1.1
Release:        3%{?dist}
Summary:        Automatic generation of record lenses for microlens

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-microlens-devel
BuildRequires:  ghc-template-haskell-devel
# End cabal-rpm deps

%description
This package lets you automatically generate lenses for data types; code was
extracted from the lens package, and therefore generated lenses are fully
compatible with ones generated by lens (and can be used both from lens and
microlens).

This package is a part of the <http://hackage.haskell.org/package/microlens
microlens> family; see the readme <https://github.com/aelve/microlens#readme on
Github>.


%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the Haskell %{pkg_name} library development files.


%prep
%setup -q -n %{pkgver}


%build
%ghc_lib_build


%install
%ghc_lib_install


%post devel
%ghc_pkg_recache


%postun devel
%ghc_pkg_recache


%files -f %{name}.files
%license LICENSE


%files devel -f %{name}-devel.files
%doc CHANGELOG.md


%changelog
* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 26 2018 Jens Petersen <petersen@redhat.com> - 0.4.1.1-2
- rebuild

* Sat Jul 22 2017 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 0.4.1.1-1
- spec file generated by cabal-rpm-0.11
