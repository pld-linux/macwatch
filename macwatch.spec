Summary:	Count in and out-bytes from one or more given ethernet devices
Summary(pl.UTF-8):	Zliczanie bajtów we/wy na urządzeniach ethernet
Name:		macwatch
Version:	0.2.7
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	http://mybox.trenger.ro/code/%{name}-current.tar.gz
# Source0-md5:	9eceaf45b02761758585acb4b29d2294
URL:		http://mybox.trenger.ro/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libpcap-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A tiny app to count in and out-bytes from one or more given
ethernet-device(s) (to and from one or more given MAC-address(es)) It
was made to enable bandwith-monitoring of spesific hosts on a lan,
i.e. a HUB-lan, usefull places where the ISP haven't enabled SNMP on
the router; or where there are server with more than one IP, and you
want to monitor the entire machine's IP-traffic.

%description -l pl.UTF-8
Niewielka aplikacja do zliczania wejściowych i wyjściowych bajtów
z jednego lub więcej urządzeń ethernet (to i z jednego lib więcej
podanych adresów MAC). Program został stworzony by umożliwić
monitorowanie pasma używanego przez określone hosty w LAN-ie użyteczne
w miejscach gdzie ISP nie udostępnia SNMP na routerze lub tam gdzie są
serwery z więcej niż jednym adresem IP, a potrzeba monitorować
sumaryczny ruch.

%prep
%setup -q -n %{name}-%{version}-5

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_sbindir}/*
