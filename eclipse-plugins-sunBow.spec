Summary:	sunBow - a collection of Eclipse plugins
Summary(pl.UTF-8):	sunBow - zestaw wtyczek do Eclipsa
Name:		eclipse-plugins-sunBow
Version:	2.0
Release:	1
License:	not precise, free for single users
Group:		Development/Languages/Java
Source0:	http://sunshine.s-und-n.de/downloads/sunBow/sunBow-plugins-%{version}.zip
# Source0-md5:	f7eea639cd7147522b78f81a11fba1de
URL:		http://radio.weblogs.com/0108489/
BuildRequires:	unzip
Requires:	eclipse
Requires:	jdk
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_eclipsedir  %{_datadir}/eclipse

%description
sunBow is a collection of Eclipse plugins that make it easier to
develop Cocoon based applications and XML solutions in general.

%description -l pl.UTF-8
sunBow jest zestawem wtyczek Eclipsa ułatwiających tworzenie aplikacji
opartych na Cocoon i, w ogólności, rozwiązaniach XML-owych.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_eclipsedir}/plugins

cp -R *  $RPM_BUILD_ROOT%{_eclipsedir}/plugins

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_eclipsedir}/plugins/de.sundn.prod.sunbow.cocoon
%{_eclipsedir}/plugins/de.sundn.prod.sunbow.core
%{_eclipsedir}/plugins/de.sundn.prod.sunbow.doc
%{_eclipsedir}/plugins/de.sundn.prod.sunbow.webapp
%{_eclipsedir}/plugins/de.sundn.prod.sunbow.xml
%{_eclipsedir}/plugins/de.sundn.prod.sunbow.log
%{_eclipsedir}/plugins/de.sundn.prod.sunbow.cocoon.debug
%{_eclipsedir}/plugins/org.apache.commons.latka
