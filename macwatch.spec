Summary:	Count in and out-bytes from one or more given ethernet devices
Summary(pl):	Zliczanie bajtów we/wy na urz±dzeniach ethernet
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

%description -l pl
Niewielka aplikacja do zliczania wej¶ciowych i wyj¶ciowych bajtów
z jednego lub wiêcej urz±dzeñ ethernet (to i z jednego lib wiêcej
podanych adresów MAC). Program zosta³ stworzony by umo¿liwiæ
monitorowanie pasma u¿ywanego przez okre¶lone hosty w LAN-ie u¿yteczne
w miejscach gdzie ISP nie udostêpnia SNMP na routerze lub tam gdzie s±
serwery z wiêcej ni¿ jednym adresem IP, a potrzeba monitorowaæ
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
