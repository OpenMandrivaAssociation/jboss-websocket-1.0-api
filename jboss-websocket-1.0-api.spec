%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jboss-websocket-1.0-api
Version:          1.0.0
Release:          2
Summary:          JSR-356: Java WebSocket 1.0 API
License:          CDDL or GPLv2 with exceptions
Url:              https://github.com/jboss/jboss-websocket-api_spec
Source0:          https://github.com/jboss/jboss-websocket-api_spec/archive/jboss-websocket-api_1.0_spec-%{namedversion}.tar.gz

BuildRequires:    jboss-parent
BuildRequires:    maven-local
BuildRequires:    felix-osgi-foundation
BuildRequires:    felix-parent

BuildArch:        noarch

%description
The JSR-356: Java WebSocket 1.0 API classes.

%package javadoc
Summary:          Javadocs for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jboss-websocket-api_spec-jboss-websocket-api_1.0_spec-%{namedversion}

%build
%mvn_alias "org.jboss.spec.javax.websocket:jboss-websocket-api_1.0_spec" "javax.websocket:javax.websocket-api" "javax.websocket:javax.websocket-client-api"
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc LICENSE README

%files javadoc -f .mfiles-javadoc
%doc LICENSE README

%changelog
* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Nov 28 2013 Marek Goldmann <mgoldman@redhat.com> - 1.0.0-1
- Upstream release 1.0.0.Final
- Add mapping to javax.websocket, RHBZ#1035718

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-0.2.Beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May 31 2013 Marek Goldmann <mgoldman@redhat.com> - 1.0.0-0.1.Beta1
- Initial packaging

