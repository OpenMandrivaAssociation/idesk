%define name idesk
%define version 0.7.5
%define release %mkrel 1

Version: 	%{version}
Summary: 	Plops icons on your root window
Name: 		%{name}
Release: 	%{release}
License: 	GPL
Group: 		Graphical desktop/Other
Source: 	%{name}-%{version}.tar.bz2
URL: 		http://idesk.sourceforge.net/
Buildrequires:	imlib2-devel gtk2-devel
Buildrequires:  libart_lgpl-devel


%description
iDesk gives users of minimal wm's (fluxbox, pekwm, windowmaker...) icons on
their desktop. The icon graphics are either from a png or svg (vector) file
and support some eyecandy effects like transparency. Each icon can be
configured to run one or more shell commands and the actions which run
those commands are completely configurable.
In a nutshell if you want icons on your desktop and you don't have or don't
want KDE or gnome doing it, you can use idesk.

%prep

%setup -q
%{__perl} -pi.orig -e 's|/usr/local/share|%_datadir|g;' examples/default.lnk

%build
%configure
%make


%install
%__rm -rf %buildroot
%makeinstall

%clean
%__rm -rf %buildroot


%files
%defattr (-,root,root)
%doc README AUTHORS ChangeLog COPYING NEWS TODO
%{_bindir}/*
%{_datadir}/%{name}/

