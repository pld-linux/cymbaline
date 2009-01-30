# TODO:
# - package gom mixer
# - fix pyao usage to choose default driver instead of hardcoded alsa
Summary:	An intelligent mp3 player
Summary(pl.UTF-8):	Inteligentny odtwarzacz mp3
Name:		cymbaline
Version:	1.3d
Release:	1
License:	GPL v2+
Group:		Applications/Sound
Source0:	http://silmarill.org/files/%{name}-%{version}.tar.gz
# Source0-md5:	633856d8743a531b2330e5bd3902d9e1
URL:		http://silmarill.org/index.html?Cymbaline
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
# FIXME: alsa output is hardcoded (instead of default)
Requires:	libao-alsa
Requires:	python-mad
Requires:	python-pyao
Suggests:	gom
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cymbaline is a learning music player. It sets a score for each track
based on your listening habits, and you can set thresholds to create
playlists with your favorite tracks automatically. In random mode, it
will play your favorite tracks more often. It also allows album-based
navigation: you can start playing the next album, skip 2 albums ahead,
go to a specific album, etc.

%description -l pl.UTF-8
Cymbaline jest uczącym się odtwarzaczem muzyki. Ustawia on punkty dla
każdego utworu słuchanego przez użytkownika, który może ustawić
progi aby program mógł automatycznie stworzyć listy odtwarzania z
ulubionych utworów. W trybie losowym program będzie częściej
odtwarzał ulubione utwory użytkownika. Umożliwia on również
nawigację opartą na albumach: przejście to następnego albumu,
przejście o 2 albumy dalej, przejście do wybranego albumu itp.

%prep
%setup -q

%{__sed} -i -e 's,"/cdrom/","/media/cdrom/",' cypack/conf.py

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_bindir}/%{name}.py $RPM_BUILD_ROOT%{_bindir}/%{name}

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/%{name}
%{py_sitescriptdir}/cypack
%{py_sitescriptdir}/cymbaline-*.egg-info
