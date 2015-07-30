UNIT                                                                                      LOAD   ACTIVE   SUB     DESCRIPTION
abrt-ccpp.service                                                                         loaded active   exited  Install ABRT coredump hook
abrt-oops.service                                                                         loaded active   running ABRT kernel log watcher
abrt-vmcore.service                                                                       loaded inactive dead    Harvest vmcores for ABRT
abrt-xorg.service                                                                         loaded active   running ABRT Xorg log watcher
abrtd.service                                                                             loaded active   running ABRT Automated Bug Reporting Tool
accounts-daemon.service                                                                   loaded active   running Accounts Service
alsa-restore.service                                                                      loaded inactive dead    Restore Sound Card State
alsa-state.service                                                                        loaded active   running Manage Sound Card State (restore and store)
alsa-store.service                                                                        loaded inactive dead    Store Sound Card State
atd.service                                                                               loaded active   running Job spooling tools
auditd.service                                                                            loaded active   running Security Auditing Service
avahi-daemon.service                                                                      loaded active   running Avahi mDNS/DNS-SD Stack
brandbot.service                                                                          loaded inactive dead    Flexible Branding Service
chronyd.service                                                                           loaded active   running NTP client/server
colord.service                                                                            loaded active   running Manage, Install and Generate Color Profiles
cpupower.service                                                                          loaded inactive dead    Configure CPU power related settings
crond.service                                                                             loaded active   running Command Scheduler
cups.service                                                                              loaded active   running CUPS Printing Service
dbus.service                                                                              loaded active   running D-Bus System Message Bus
dm-event.service                                                                          loaded inactive dead    Device-mapper event daemon
dmraid-activation.service                                                                 loaded inactive dead    Activation of DM RAID sets
dracut-shutdown.service                                                                   loaded inactive dead    Restore /run/initramfs
ebtables.service                                                                          loaded inactive dead    Ethernet Bridge Filtering tables
emergency.service                                                                         loaded inactive dead    Emergency Shell
exim.service                                                                              not-found inactive dead    exim.service
firewalld.service                                                                         loaded active   running firewalld - dynamic firewall daemon
fprintd.service                                                                           loaded failed   failed  Fingerprint Authentication Daemon
gdm.service                                                                               loaded active   running GNOME Display Manager
getty@tty1.service                                                                        loaded inactive dead    Getty on tty1
httpd.service                                                                             loaded inactive dead    The Apache HTTP Server
ip6tables.service                                                                         loaded inactive dead    IPv6 firewall with ip6tables
iprdump.service                                                                           loaded active   running LSB: Start the ipr dump daemon
iprinit.service                                                                           loaded active   running LSB: Start the ipr init daemon
iprupdate.service                                                                         loaded active   running LSB: Start the iprupdate utility
iptables.service                                                                          loaded inactive dead    IPv4 firewall with iptables
irqbalance.service                                                                        loaded active   running irqbalance daemon
iscsi.service                                                                             loaded inactive dead    Login and scanning of iSCSI devices
iscsid.service                                                                            loaded inactive dead    Open-iSCSI
iscsiuio.service                                                                          loaded inactive dead    iSCSI UserSpace I/O driver
kdump.service                                                                             loaded active   exited  Crash recovery kernel arming
kmod-static-nodes.service                                                                 loaded active   exited  Create list of required static device nodes for the current kernel
ksm.service                                                                               loaded active   exited  Kernel Samepage Merging
ksmtuned.service                                                                          loaded active   running Kernel Samepage Merging (KSM) Tuning Daemon
libstoragemgmt.service                                                                    loaded active   running libstoragemgmt plug-in server daemon
libvirt-guests.service                                                                    loaded inactive dead    Suspend Active Libvirt Guests
libvirtd.service                                                                          loaded active   running Virtualization daemon
livesys.service                                                                           not-found inactive dead    livesys.service
lvm2-activation-early.service                                                             not-found inactive dead    lvm2-activation-early.service
lvm2-activation.service                                                                   not-found inactive dead    lvm2-activation.service
lvm2-lvmetad.service                                                                      loaded active   running LVM2 metadata daemon
lvm2-monitor.service                                                                      loaded active   exited  Monitoring of LVM2 mirrors, snapshots etc. using dmeventd or progress polling
lvm2-pvscan@8:2.service                                                                   loaded active   exited  LVM2 PV scan on device 8:2
mariadb.service                                                                           loaded active   running MariaDB database server
mdmonitor.service                                                                         loaded inactive dead    Software RAID monitoring and management
microcode.service                                                                         loaded inactive dead    Load CPU microcode update
ModemManager.service                                                                      loaded active   running Modem Manager
multipathd.service                                                                        loaded inactive dead    Device-Mapper Multipath Device Controller
named.service                                                                             not-found inactive dead    named.service
netcf-transaction.service                                                                 loaded active   exited  Rollback uncommitted netcf network config change transactions
netconsole.service                                                                        loaded inactive dead    SYSV: Initializes network console logging
network.service                                                                           loaded active   exited  LSB: Bring up/down networking
NetworkManager-dispatcher.service                                                         loaded active   running Network Manager Script Dispatcher Service
NetworkManager-wait-online.service                                                        loaded inactive dead    Network Manager Wait Online
NetworkManager.service                                                                    loaded active   running Network Manager
nfs-lock.service                                                                          loaded active   running NFS file locking service.
nmb.service                                                                               loaded inactive dead    Samba NMB Daemon
ntpd.service                                                                              loaded inactive dead    Network Time Service
ntpdate.service                                                                           loaded inactive dead    Set time via NTP
plymouth-quit-wait.service                                                                loaded inactive dead    Wait for Plymouth Boot Screen to Quit
plymouth-quit.service                                                                     loaded inactive dead    Terminate Plymouth Boot Screen
plymouth-read-write.service                                                               loaded inactive dead    Tell Plymouth To Write Out Runtime Data
plymouth-start.service                                                                    loaded inactive dead    Show Plymouth Boot Screen
pmcd.service                                                                              loaded inactive dead    LSB: Control pmcd (the collection daemon for PCP)
pmie.service                                                                              loaded inactive dead    LSB: Control pmie (performance inference engine for PCP)
pmlogger.service                                                                          loaded inactive dead    LSB: Control pmlogger (the performance metrics logger for PCP)
pmmgr.service                                                                             loaded inactive dead    LSB: Control pmmgr (daemon manager for PCP)
pmproxy.service                                                                           loaded inactive dead    LSB: Control pmproxy (the pmcd proxy daemon for PCP)
pmwebd.service                                                                            loaded inactive dead    LSB: Control pmwebd (the web frontend for PCP)
polkit.service                                                                            loaded active   running Authorization Manager
postfix.service                                                                           loaded active   running Postfix Mail Transport Agent
rc-local.service                                                                          loaded inactive dead    /etc/rc.d/rc.local Compatibility
rescue.service                                                                            loaded inactive dead    Rescue Shell
rhel-autorelabel-mark.service                                                             loaded inactive dead    Mark the need to relabel after reboot
rhel-autorelabel.service                                                                  loaded inactive dead    Relabel all filesystems, if necessary
rhel-configure.service                                                                    loaded inactive dead    Reconfigure the system on administrator request
rhel-dmesg.service                                                                        loaded active   exited  Dump dmesg to /var/log/dmesg
rhel-import-state.service                                                                 loaded active   exited  Import network configuration from initramfs
rhel-loadmodules.service                                                                  loaded active   exited  Load legacy module configuration
rhel-readonly.service                                                                     loaded active   exited  Configure read-only root support
rngd.service                                                                              loaded failed   failed  Hardware RNG Entropy Gatherer Daemon
rpcbind.service                                                                           loaded active   running RPC bind service
rsyslog.service                                                                           loaded active   running System Logging Service
rtkit-daemon.service                                                                      loaded active   running RealtimeKit Scheduling Policy Service
sendmail.service                                                                          not-found inactive dead    sendmail.service
smartd.service                                                                            loaded active   running Self Monitoring and Reporting Technology (SMART) Daemon
smb.service                                                                               loaded active   running Samba SMB Daemon
sntp.service                                                                              not-found inactive dead    sntp.service
sshd.service                                                                              loaded active   running OpenSSH server daemon
syslog.service                                                                            not-found inactive dead    syslog.service
sysstat.service                                                                           loaded active   exited  Resets System Activity Logs
systemd-ask-password-console.service                                                      loaded inactive dead    Dispatch Password Requests to Console
systemd-ask-password-plymouth.service                                                     loaded inactive dead    Forward Password Requests to Plymouth
systemd-ask-password-wall.service                                                         loaded inactive dead    Forward Password Requests to Wall
systemd-binfmt.service                                                                    loaded inactive dead    Set Up Additional Binary Formats
systemd-fsck-root.service                                                                 loaded active   exited  File System Check on Root Device
systemd-fsck@dev-disk-by\x2duuid-011d960d\x2d4ffc\x2d4658\x2d951b\x2d8cd1a4fd3e6e.service loaded active   exited  File System Check on /dev/disk/by-uuid/011d960d-4ffc-4658-951b-8cd1a4fd3e6e
systemd-initctl.service                                                                   loaded inactive dead    /dev/initctl Compatibility Daemon
systemd-journal-flush.service                                                             loaded inactive dead    Trigger Flushing of Journal to Persistent Storage
systemd-journald.service                                                                  loaded active   running Journal Service
systemd-logind.service                                                                    loaded active   running Login Service
systemd-modules-load.service                                                              loaded inactive dead    Load Kernel Modules
systemd-random-seed-load.service                                                          not-found inactive dead    systemd-random-seed-load.service
systemd-random-seed.service                                                               loaded active   exited  Load/Save Random Seed
systemd-readahead-collect.service                                                         loaded inactive dead    Collect Read-Ahead Data
systemd-readahead-done.service                                                            loaded inactive dead    Stop Read-Ahead Data Collection
systemd-readahead-replay.service                                                          loaded inactive dead    Replay Read-Ahead Data
systemd-reboot.service                                                                    loaded inactive dead    Reboot
systemd-remount-fs.service                                                                loaded active   exited  Remount Root and Kernel File Systems
systemd-shutdownd.service                                                                 loaded inactive dead    Delayed Shutdown Service
systemd-sysctl.service                                                                    loaded active   exited  Apply Kernel Variables
systemd-tmpfiles-clean.service                                                            loaded inactive dead    Cleanup of Temporary Directories
systemd-tmpfiles-setup-dev.service                                                        loaded active   exited  Create static device nodes in /dev
systemd-tmpfiles-setup.service                                                            loaded active   exited  Create Volatile Files and Directories
systemd-udev-settle.service                                                               loaded active   exited  udev Wait for Complete Device Initialization
systemd-udev-trigger.service                                                              loaded active   exited  udev Coldplug all Devices
systemd-udevd.service                                                                     loaded active   running udev Kernel Device Manager
systemd-update-utmp-runlevel.service                                                      loaded inactive dead    Update UTMP about System Runlevel Changes
systemd-update-utmp.service                                                               loaded active   exited  Update UTMP about System Reboot/Shutdown
systemd-user-sessions.service                                                             loaded active   exited  Permit User Sessions
systemd-vconsole-setup.service                                                            loaded active   exited  Setup Virtual Console
tuned.service                                                                             loaded active   running Dynamic System Tuning Daemon
upower.service                                                                            loaded active   running Daemon for power management
vmtoolsd.service                                                                          loaded active   running Service for virtual machines hosted on VMware
winbind.service                                                                           loaded inactive dead    Samba Winbind Daemon

LOAD   = Reflects whether the unit definition was properly loaded.
ACTIVE = The high-level unit activation state, i.e. generalization of SUB.
SUB    = The low-level unit activation state, values depend on unit type.

134 loaded units listed.
To show all installed unit files use 'systemctl list-unit-files'.
