%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name nan
%{?nodejs_find_provides_and_requires}

Summary:       Native Abstractions for Node.js 
Name:          %{?scl_prefix}nodejs-%{npm_name}
Version:       0.4.4
Release:       2.2.sc1%{?dist}
Group:         Development/Languages
License:       MIT
URL:           http://github.com/rvagg/nan
Source0:       http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: %{?scl_prefix}nodejs-devel
%if 0%{?enable_tests}
BuildRequires:  %{?scl_prefix}npm()
%endif
BuildArch:     noarch

%description
A header file filled with macro and utility goodness
for making add on development for Node.js easier across
versions 0.8, 0.10 and 0.11, and eventually 0.12.

Thanks to the crazy changes in V8 (and some in Node core),
keeping native add-on compiling happily across versions,
particularly 0.10 to 0.11/0.12, is a minor nightmare. 
The goal of this project is to store all logic necessary
to develop native Node.js add-on without having to inspect 
NODE_MODULE_VERSION and get yourself into a macro-tangle.

%prep
%setup -q -n package

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr .index.js nan.h package.json  %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%files
%doc LICENSE README.md
%{nodejs_sitelib}/%{npm_name}

%changelog
* Tue Mar 04 2014 Tomas Hrcka <thrcka@redhat.com> - 0.4.4-2.2
- Add missing nodejs_symlink_deps macro

* Tue Jan 14 2014 Tomas Hrcka <thrcka@redhat.com> - 0.4.4-1.2
- Add provides requires macro

* Thu Jan 09 2014 Tomas Hrcka <thrcka@redhat.com> - 0.4.4-1.1
- enable scl support

* Fri Nov 08 2013 Troy Dawson <tdawson@redhat.com> - 0.4.4-1
- Update to 0.4.4

* Mon Oct 07 2013 Troy Dawson <tdawson@redhat.com> - 0.4.1-1
- Initial build
