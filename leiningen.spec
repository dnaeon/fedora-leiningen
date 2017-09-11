%global debug_package %{nil}
%global _enable_debug_package 0
%global __os_install_post /usr/lib/rpm/brp-compress %{nil}

Name:          leiningen
Version:       2.7.1
Release:       1%{?dist}
Summary:       The easiest way to use Clojure

URL:           https://leiningen.org
Group:         Development/Languages
License:       EPL

BuildArch:     noarch

Requires:      java-headless
BuildRequires: java-headless

Source0: https://github.com/technomancy/%{name}/archive/%{version}.tar.gz
Source1: https://github.com/technomancy/%{name}/releases/download/%{version}/%{name}-%{version}-standalone.zip

%description
Automate Clojure projects without setting your hair on fire.

With a focus on project automation and declarative configuration,
it gets out of your way and lets you focus on your code.

%prep
%autosetup

%build

%install
install -m 755 -D bin/lein-pkg %{buildroot}%{_bindir}/lein
install -D doc/lein.1 %{buildroot}%{_mandir}/man1/lein.1
install -D %{SOURCE1} %{buildroot}%{_datadir}/java/%{name}-%{version}-standalone.jar

%check

%files
%doc CONTRIBUTING.md TUTORIAL.md README.md NEWS.md
%license COPYING
%{_bindir}/lein
%{_mandir}/man1/*
%{_datadir}/java/%{name}-%{version}-standalone.jar

%changelog
* Sun Sep 10 2017 Médéric Hurier <med.hur@gmail.com> - 2.7.1-1
- Initial packaging.
