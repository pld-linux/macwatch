Summary:	Count in and out-bytes from one or more given ethernet devices
Summary(pl):	Zliczanie bajt�w we/wy na urz�dzeniach ethernet
Name:		macwatch
Version:	0.2.7
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	%{name}-current.tar.gz
URL:		http://mybox.trenger.ro/
BuildRequires:	libpcap-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A tiny app to count in and out-bytes from one or more given
ethernet-device(s) (to and from one or more given MAC-address(es)) It
was made to enable bandwith-monitoring of spesific hosts on a lan,
i.e. a HUB-lan, usefull places where the ISP haven't enabled SNMP on
the router; or where there are server with more than one IP, and you
want to monitor the entire machine's IP-traffic.

%description -l pl
Niewielka aplikacja do zliczania wej�ciowych i wyj�ciowych bajt�w
z jednego lub wi�cej urz�dze� ethernet (to i z jednego lib wi�cej
podanych adres�w MAC). Program zosta� stworzony by umo�liwi� monitorowanie
pasma u�ywanego przez okre�lone hosty w LANie u�yteczne w miejscach
gdzie ISP nie udost�pnia SNMP na routerze lub tam gdzie s� serwery
z wi�cej ni� jednym adresem IP, a potrzeba monitorowa� sumaryczny
ruch.

%prep
%setup -q -n %{name}-%{version}-4

%build
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