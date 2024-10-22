# Table of Contents

## Terms of Use ................................................................................................................. 1

 Table of Contents .......................................................................................................... 2

 Overview ...................................................................................................................... 11

### Intended Audience ................................................................................................................11

 Consensus Guidance ...........................................................................................................12

 Typographical Conventions .................................................................................................13

## Recommendation Definitions ..................................................................................... 14

### Title ........................................................................................................................................14

 Assessment Status ...............................................................................................................14

**Automated ............................................................................................................................................ 14**
**Manual ................................................................................................................................................... 14**

### Profile ....................................................................................................................................14

 Description ............................................................................................................................14

 Rationale Statement .............................................................................................................14

 Impact Statement ..................................................................................................................15

 Audit Procedure ....................................................................................................................15

 Remediation Procedure ........................................................................................................15

 Default Value .........................................................................................................................15

 References ............................................................................................................................15

 CIS Critical Security Controls[®] (CIS Controls[®]) ..................................................................15

 Additional Information..........................................................................................................15

 Profile Definitions .................................................................................................................16

 Acknowledgements ..............................................................................................................17

## Recommendations ...................................................................................................... 18

### 1 Initial Setup ........................................................................................................................18

**1.1 Filesystem ...................................................................................................................................... 19**

**1.1.1 Configure Filesystem Kernel Modules ................................................................................... 20**

1.1.1.1 Ensure cramfs kernel module is not available (Automated) ......................................... 21
1.1.1.2 Ensure freevxfs kernel module is not available (Automated) ....................................... 26
1.1.1.3 Ensure hfs kernel module is not available (Automated) ............................................... 31
1.1.1.4 Ensure hfsplus kernel module is not available (Automated) ........................................ 36
1.1.1.5 Ensure jffs2 kernel module is not available (Automated) ............................................. 41
1.1.1.6 Ensure squashfs kernel module is not available (Automated) ..................................... 46
1.1.1.7 Ensure udf kernel module is not available (Automated) ............................................... 51
1.1.1.8 Ensure usb-storage kernel module is not available (Automated) ................................. 56

**1.1.2 Configure Filesystem Partitions ............................................................................................. 61**

**1.1.2.1 Configure /tmp .................................................................................................................... 62**


Page 2


-----

1.1.2.1.1 Ensure /tmp is a separate partition (Automated) ....................................................... 63
1.1.2.1.2 Ensure nodev option set on /tmp partition (Automated) ............................................ 67
1.1.2.1.3 Ensure nosuid option set on /tmp partition (Automated) ........................................... 69
1.1.2.1.4 Ensure noexec option set on /tmp partition (Automated) .......................................... 71

**1.1.2.2 Configure /dev/shm ............................................................................................................ 73**

1.1.2.2.1 Ensure /dev/shm is a separate partition (Automated) ............................................... 74
1.1.2.2.2 Ensure nodev option set on /dev/shm partition (Automated) .................................... 76
1.1.2.2.3 Ensure nosuid option set on /dev/shm partition (Automated) .................................... 78
1.1.2.2.4 Ensure noexec option set on /dev/shm partition (Automated) ................................... 80

**1.1.2.3 Configure /home ................................................................................................................. 82**

1.1.2.3.1 Ensure separate partition exists for /home (Automated) ........................................... 83
1.1.2.3.2 Ensure nodev option set on /home partition (Automated) ......................................... 85
1.1.2.3.3 Ensure nosuid option set on /home partition (Automated) ........................................ 87

**1.1.2.4 Configure /var ..................................................................................................................... 89**

1.1.2.4.1 Ensure separate partition exists for /var (Automated) ............................................... 90
1.1.2.4.2 Ensure nodev option set on /var partition (Automated) ............................................. 93
1.1.2.4.3 Ensure nosuid option set on /var partition (Automated) ............................................ 95

**1.1.2.5 Configure /var/tmp .............................................................................................................. 97**

1.1.2.5.1 Ensure separate partition exists for /var/tmp (Automated) ........................................ 98
1.1.2.5.2 Ensure nodev option set on /var/tmp partition (Automated) .................................... 100
1.1.2.5.3 Ensure nosuid option set on /var/tmp partition (Automated) ................................... 102
1.1.2.5.4 Ensure noexec option set on /var/tmp partition (Automated) .................................. 104

**1.1.2.6 Configure /var/log ............................................................................................................. 106**

1.1.2.6.1 Ensure separate partition exists for /var/log (Automated) ....................................... 107
1.1.2.6.2 Ensure nodev option set on /var/log partition (Automated) ..................................... 109
1.1.2.6.3 Ensure nosuid option set on /var/log partition (Automated) .................................... 111
1.1.2.6.4 Ensure noexec option set on /var/log partition (Automated) ................................... 113

**1.1.2.7 Configure /var/log/audit ................................................................................................... 115**

1.1.2.7.1 Ensure separate partition exists for /var/log/audit (Automated) .............................. 116
1.1.2.7.2 Ensure nodev option set on /var/log/audit partition (Automated) ............................ 118
1.1.2.7.3 Ensure nosuid option set on /var/log/audit partition (Automated) ............................ 120
1.1.2.7.4 Ensure noexec option set on /var/log/audit partition (Automated)........................... 122

**1.2 Package Management ................................................................................................................. 124**

**1.2.1 Configure Package Repositories .......................................................................................... 125**

1.2.1.1 Ensure GPG keys are configured (Manual) ................................................................ 126
1.2.1.2 Ensure package manager repositories are configured (Manual) ............................... 128

**1.2.2 Configure Package Updates ................................................................................................. 130**

1.2.2.1 Ensure updates, patches, and additional security software are installed (Manual) ... 131

**1.3 Mandatory Access Control ......................................................................................................... 134**

**1.3.1 Configure AppArmor.............................................................................................................. 135**

1.3.1.1 Ensure AppArmor is installed (Automated) ................................................................ 136
1.3.1.2 Ensure AppArmor is enabled in the bootloader configuration (Automated) ............... 138
1.3.1.3 Ensure all AppArmor Profiles are in enforce or complain mode (Automated) ............ 140
1.3.1.4 Ensure all AppArmor Profiles are enforcing (Automated) .......................................... 142

**1.4 Configure Bootloader .................................................................................................................. 144**

1.4.1 Ensure bootloader password is set (Automated) ........................................................... 145
1.4.2 Ensure access to bootloader config is configured (Automated) .................................... 148

**1.5 Configure Additional Process Hardening ................................................................................. 150**

1.5.1 Ensure address space layout randomization is enabled (Automated) .......................... 151
1.5.2 Ensure ptrace_scope is restricted (Automated) ............................................................ 155
1.5.3 Ensure core dumps are restricted (Automated) ............................................................. 159
1.5.4 Ensure prelink is not installed (Automated) ................................................................... 162
1.5.5 Ensure Automatic Error Reporting is not enabled (Automated) .................................... 164

**1.6 Configure Command Line Warning Banners ............................................................................ 166**

1.6.1 Ensure message of the day is configured properly (Automated) .................................. 167
1.6.2 Ensure local login warning banner is configured properly (Automated) ........................ 169

Page 3


-----

1.6.3 Ensure remote login warning banner is configured properly (Automated) .................... 171
1.6.4 Ensure access to /etc/motd is configured (Automated) ................................................. 173
1.6.5 Ensure access to /etc/issue is configured (Automated)................................................. 175
1.6.6 Ensure access to /etc/issue.net is configured (Automated) .......................................... 177

**1.7 Configure GNOME Display Manager .......................................................................................... 179**

1.7.1 Ensure GDM is removed (Automated) .......................................................................... 180
1.7.2 Ensure GDM login banner is configured (Automated) ................................................... 182
1.7.3 Ensure GDM disable-user-list option is enabled (Automated) ...................................... 186
1.7.4 Ensure GDM screen locks when the user is idle (Automated) ...................................... 190
1.7.5 Ensure GDM screen locks cannot be overridden (Automated) ..................................... 193
1.7.6 Ensure GDM automatic mounting of removable media is disabled (Automated) .......... 196
1.7.7 Ensure GDM disabling automatic mounting of removable media is not overridden
(Automated) ............................................................................................................................ 202
1.7.8 Ensure GDM autorun-never is enabled (Automated) .................................................... 205
1.7.9 Ensure GDM autorun-never is not overridden (Automated) .......................................... 210
1.7.10 Ensure XDCMP is not enabled (Automated) ............................................................... 213


### 2 Services ............................................................................................................................ 216

**2.1 Configure Server Services .......................................................................................................... 217**

2.1.1 Ensure autofs services are not in use (Automated) ....................................................... 218
2.1.2 Ensure avahi daemon services are not in use (Automated) .......................................... 221
2.1.3 Ensure dhcp server services are not in use (Automated).............................................. 224
2.1.4 Ensure dns server services are not in use (Automated)................................................ 227
2.1.5 Ensure dnsmasq services are not in use (Automated) .................................................. 229
2.1.6 Ensure ftp server services are not in use (Automated) ................................................. 232
2.1.7 Ensure ldap server services are not in use (Automated)............................................... 235
2.1.8 Ensure message access server services are not in use (Automated) .......................... 238
2.1.9 Ensure network file system services are not in use (Automated) .................................. 242
2.1.10 Ensure nis server services are not in use (Automated) ............................................... 245
2.1.11 Ensure print server services are not in use (Automated) ............................................ 248
2.1.12 Ensure rpcbind services are not in use (Automated)................................................... 251
2.1.13 Ensure rsync services are not in use (Automated) ...................................................... 254
2.1.14 Ensure samba file server services are not in use (Automated) ................................... 257
2.1.15 Ensure snmp services are not in use (Automated) ...................................................... 260
2.1.16 Ensure tftp server services are not in use (Automated) .............................................. 263
2.1.17 Ensure web proxy server services are not in use (Automated) ................................... 266
2.1.18 Ensure web server services are not in use (Automated) ............................................. 269
2.1.19 Ensure xinetd services are not in use (Automated) ..................................................... 273
2.1.20 Ensure X window server services are not in use (Automated) .................................... 276
2.1.21 Ensure mail transfer agent is configured for local-only mode (Automated) ................ 278
2.1.22 Ensure only approved services are listening on a network interface (Manual) ........... 281

**2.2 Configure Client Services ........................................................................................................... 284**

2.2.1 Ensure NIS Client is not installed (Automated) ............................................................. 285
2.2.2 Ensure rsh client is not installed (Automated) ............................................................... 287
2.2.3 Ensure talk client is not installed (Automated) ............................................................... 289
2.2.4 Ensure telnet client is not installed (Automated) ........................................................... 291
2.2.5 Ensure ldap client is not installed (Automated) ............................................................. 293
2.2.6 Ensure ftp client is not installed (Automated) ................................................................ 295

**2.3 Configure Time Synchronization ............................................................................................... 297**

**2.3.1 Ensure time synchronization is in use................................................................................. 298**

2.3.1.1 Ensure a single time synchronization daemon is in use (Automated) ........................ 299

**2.3.2 Configure systemd-timesyncd .............................................................................................. 303**

2.3.2.1 Ensure systemd-timesyncd configured with authorized timeserver (Automated) ...... 305
2.3.2.2 Ensure systemd-timesyncd is enabled and running (Manual) .................................... 309

**2.3.3 Configure chrony ................................................................................................................... 311**

2.3.3.1 Ensure chrony is configured with authorized timeserver (Manual) ............................. 312

Page 4


-----

2.3.3.2 Ensure chrony is running as user _chrony (Automated) ............................................ 316
2.3.3.3 Ensure chrony is enabled and running (Automated) .................................................. 318

**2.4 Job Schedulers ............................................................................................................................ 320**

**2.4.1 Configure cron ........................................................................................................................ 321**

2.4.1.1 Ensure cron daemon is enabled and active (Automated) .......................................... 322
2.4.1.2 Ensure permissions on /etc/crontab are configured (Automated) .............................. 324
2.4.1.3 Ensure permissions on /etc/cron.hourly are configured (Automated) ........................ 326
2.4.1.4 Ensure permissions on /etc/cron.daily are configured (Automated) ........................... 328
2.4.1.5 Ensure permissions on /etc/cron.weekly are configured (Automated) ....................... 330
2.4.1.6 Ensure permissions on /etc/cron.monthly are configured (Automated)...................... 332
2.4.1.7 Ensure permissions on /etc/cron.d are configured (Automated) ................................ 334
2.4.1.8 Ensure crontab is restricted to authorized users (Automated) ................................... 336

**2.4.2 Configure at ............................................................................................................................ 340**

2.4.2.1 Ensure at is restricted to authorized users (Automated) ............................................ 341


### 3 Network ............................................................................................................................ 345

**3.1 Configure Network Devices ........................................................................................................ 346**

3.1.1 Ensure IPv6 status is identified (Manual) ...................................................................... 347
3.1.2 Ensure wireless interfaces are disabled (Automated) ................................................... 350
3.1.3 Ensure bluetooth services are not in use (Automated).................................................. 354

**3.2 Configure Network Kernel Modules ........................................................................................... 357**

3.2.1 Ensure dccp kernel module is not available (Automated) ............................................. 358
3.2.2 Ensure tipc kernel module is not available (Automated) ............................................... 363
3.2.3 Ensure rds kernel module is not available (Automated) ................................................ 368
3.2.4 Ensure sctp kernel module is not available (Automated) .............................................. 373

**3.3 Configure Network Kernel Parameters ...................................................................................... 378**

3.3.1 Ensure ip forwarding is disabled (Automated) ............................................................... 379
3.3.2 Ensure packet redirect sending is disabled (Automated) .............................................. 383
3.3.3 Ensure bogus icmp responses are ignored (Automated) .............................................. 387
3.3.4 Ensure broadcast icmp requests are ignored (Automated) ........................................... 391
3.3.5 Ensure icmp redirects are not accepted (Automated) ................................................... 395
3.3.6 Ensure secure icmp redirects are not accepted (Automated) ....................................... 399
3.3.7 Ensure reverse path filtering is enabled (Automated) ................................................... 403
3.3.8 Ensure source routed packets are not accepted (Automated) ...................................... 407
3.3.9 Ensure suspicious packets are logged (Automated) ..................................................... 412
3.3.10 Ensure tcp syn cookies is enabled (Automated) ......................................................... 416
3.3.11 Ensure ipv6 router advertisements are not accepted (Automated) ............................. 420

### 4 Host Based Firewall ......................................................................................................... 424

**4.1 Configure UncomplicatedFirewall .............................................................................................. 425**

4.1.1 Ensure ufw is installed (Automated) .............................................................................. 426
4.1.2 Ensure iptables-persistent is not installed with ufw (Automated) .................................. 428
4.1.3 Ensure ufw service is enabled (Automated) .................................................................. 430
4.1.4 Ensure ufw loopback traffic is configured (Automated) ................................................. 433
4.1.5 Ensure ufw outbound connections are configured (Manual) ......................................... 435
4.1.6 Ensure ufw firewall rules exist for all open ports (Automated) ...................................... 437
4.1.7 Ensure ufw default deny firewall policy (Automated) ..................................................... 440

**4.2 Configure nftables ....................................................................................................................... 442**

4.2.1 Ensure nftables is installed (Automated) ....................................................................... 445
4.2.2 Ensure ufw is uninstalled or disabled with nftables (Automated) .................................. 447
4.2.3 Ensure iptables are flushed with nftables (Manual) ....................................................... 449
4.2.4 Ensure a nftables table exists (Automated) ................................................................... 451
4.2.5 Ensure nftables base chains exist (Automated) ............................................................ 453
4.2.6 Ensure nftables loopback traffic is configured (Automated) .......................................... 455
4.2.7 Ensure nftables outbound and established connections are configured (Manual) ........ 457
4.2.8 Ensure nftables default deny firewall policy (Automated) .............................................. 460
4.2.9 Ensure nftables service is enabled (Automated) ........................................................... 463

Page 5


-----

4.2.10 Ensure nftables rules are permanent (Automated) ...................................................... 465

**4.3 Configure iptables ....................................................................................................................... 468**

**4.3.1 Configure iptables software .................................................................................................. 469**

4.3.1.1 Ensure iptables packages are installed (Automated) ................................................. 470
4.3.1.2 Ensure nftables is not installed with iptables (Automated) ......................................... 472
4.3.1.3 Ensure ufw is uninstalled or disabled with iptables (Automated) ............................... 474

**4.3.2 Configure IPv4 iptables ......................................................................................................... 476**

4.3.2.1 Ensure iptables default deny firewall policy (Automated) ........................................... 477
4.3.2.2 Ensure iptables loopback traffic is configured (Automated) ....................................... 479
4.3.2.3 Ensure iptables outbound and established connections are configured (Manual) ..... 481
4.3.2.4 Ensure iptables firewall rules exist for all open ports (Automated) ............................. 483

**4.3.3 Configure IPv6 ip6tables ....................................................................................................... 486**

4.3.3.1 Ensure ip6tables default deny firewall policy (Automated) ......................................... 487
4.3.3.2 Ensure ip6tables loopback traffic is configured (Automated) ..................................... 490
4.3.3.3 Ensure ip6tables outbound and established connections are configured (Manual) ... 493
4.3.3.4 Ensure ip6tables firewall rules exist for all open ports (Automated) ........................... 495


### 5 Access Control ................................................................................................................ 498

**5.1 Configure SSH Server ................................................................................................................. 499**

5.1.1 Ensure permissions on /etc/ssh/sshd_config are configured (Automated) ................... 501
5.1.2 Ensure permissions on SSH private host key files are configured (Automated) ........... 504
5.1.3 Ensure permissions on SSH public host key files are configured (Automated) ............ 508
5.1.4 Ensure sshd access is configured (Automated) ............................................................ 512
5.1.5 Ensure sshd Banner is configured (Automated) ............................................................ 515
5.1.6 Ensure sshd Ciphers are configured (Automated) ........................................................ 517
5.1.7 Ensure sshd ClientAliveInterval and ClientAliveCountMax are configured (Automated)
................................................................................................................................................ 520
5.1.8 Ensure sshd DisableForwarding is enabled (Automated) ............................................. 523
5.1.9 Ensure sshd GSSAPIAuthentication is disabled (Automated) ...................................... 526
5.1.10 Ensure sshd HostbasedAuthentication is disabled (Automated) ................................. 528
5.1.11 Ensure sshd IgnoreRhosts is enabled (Automated) .................................................... 530
5.1.12 Ensure sshd KexAlgorithms is configured (Automated) .............................................. 532
5.1.13 Ensure sshd LoginGraceTime is configured (Automated) ........................................... 535
5.1.14 Ensure sshd LogLevel is configured (Automated) ....................................................... 537
5.1.15 Ensure sshd MACs are configured (Automated) ......................................................... 539
5.1.16 Ensure sshd MaxAuthTries is configured (Automated) ............................................... 542
5.1.17 Ensure sshd MaxSessions is configured (Automated) ................................................ 544
5.1.18 Ensure sshd MaxStartups is configured (Automated) ................................................. 546
5.1.19 Ensure sshd PermitEmptyPasswords is disabled (Automated) .................................. 548
5.1.20 Ensure sshd PermitRootLogin is disabled (Automated) .............................................. 550
5.1.21 Ensure sshd PermitUserEnvironment is disabled (Automated) .................................. 552
5.1.22 Ensure sshd UsePAM is enabled (Automated) ........................................................... 554

**5.2 Configure privilege escalation ................................................................................................... 556**

5.2.1 Ensure sudo is installed (Automated) ............................................................................ 557
5.2.2 Ensure sudo commands use pty (Automated) .............................................................. 559
5.2.3 Ensure sudo log file exists (Automated) ........................................................................ 562
5.2.4 Ensure users must provide password for privilege escalation (Automated) ................. 564
5.2.5 Ensure re-authentication for privilege escalation is not disabled globally (Automated) 566
5.2.6 Ensure sudo authentication timeout is configured correctly (Automated) ..................... 568
5.2.7 Ensure access to the su command is restricted (Automated) ....................................... 570

**5.3 Pluggable Authentication Modules ............................................................................................ 572**

**5.3.1 Configure PAM software packages ...................................................................................... 573**

5.3.1.1 Ensure latest version of pam is installed (Automated) ............................................... 574
5.3.1.2 Ensure libpam-modules is installed (Automated) ....................................................... 575
5.3.1.3 Ensure libpam-pwquality is installed (Automated) ...................................................... 576

**5.3.2 Configure pam-auth-update profiles .................................................................................... 577**

Page 6


-----

5.3.2.1 Ensure pam_unix module is enabled (Automated)..................................................... 578
5.3.2.2 Ensure pam_faillock module is enabled (Automated) ................................................ 580
5.3.2.3 Ensure pam_pwquality module is enabled (Automated) ............................................ 583
5.3.2.4 Ensure pam_pwhistory module is enabled (Automated) ............................................ 586

**5.3.3 Configure PAM Arguments ................................................................................................... 589**

**5.3.3.1 Configure pam_faillock module ...................................................................................... 590**

5.3.3.1.1 Ensure password failed attempts lockout is configured (Automated)...................... 591
5.3.3.1.2 Ensure password unlock time is configured (Automated) ....................................... 593
5.3.3.1.3 Ensure password failed attempts lockout includes root account (Automated) ........ 596

**5.3.3.2 Configure pam_pwquality module .................................................................................. 599**

5.3.3.2.1 Ensure password number of changed characters is configured (Automated) ........ 601
5.3.3.2.2 Ensure minimum password length is configured (Automated) ................................ 605
5.3.3.2.3 Ensure password complexity is configured (Manual) .............................................. 609
5.3.3.2.4 Ensure password same consecutive characters is configured (Automated) ........... 613
5.3.3.2.5 Ensure password maximum sequential characters is configured (Automated) ...... 617
5.3.3.2.6 Ensure password dictionary check is enabled (Automated) .................................... 621
5.3.3.2.7 Ensure password quality checking is enforced (Automated) ................................... 624
5.3.3.2.8 Ensure password quality is enforced for the root user (Automated) ....................... 626

**5.3.3.3 Configure pam_pwhistory module ................................................................................. 629**

5.3.3.3.1 Ensure password history remember is configured (Automated) ............................. 630
5.3.3.3.2 Ensure password history is enforced for the root user (Automated) ....................... 633
5.3.3.3.3 Ensure pam_pwhistory includes use_authtok (Automated) .................................... 636

**5.3.3.4 Configure pam_unix module ........................................................................................... 638**

5.3.3.4.1 Ensure pam_unix does not include nullok (Automated) .......................................... 639
5.3.3.4.2 Ensure pam_unix does not include remember (Automated) ................................... 642
5.3.3.4.3 Ensure pam_unix includes a strong password hashing algorithm (Automated) ..... 644
5.3.3.4.4 Ensure pam_unix includes use_authtok (Automated) ............................................. 648

**5.4 User Accounts and Environment ............................................................................................... 651**

**5.4.1 Configure shadow password suite parameters .................................................................. 652**

5.4.1.1 Ensure password expiration is configured (Automated) ............................................. 653
5.4.1.2 Ensure minimum password age is configured (Manual) ............................................ 657
5.4.1.3 Ensure password expiration warning days is configured (Automated) ....................... 660
5.4.1.4 Ensure strong password hashing algorithm is configured (Automated) ..................... 662
5.4.1.5 Ensure inactive password lock is configured (Automated) ......................................... 665
5.4.1.6 Ensure all users last password change date is in the past (Automated) .................... 668

**5.4.2 Configure root and system accounts and environment .................................................... 670**

5.4.2.1 Ensure root is the only UID 0 account (Automated) ................................................... 671
5.4.2.2 Ensure root is the only GID 0 account (Automated) ................................................... 672
5.4.2.3 Ensure group root is the only GID 0 group (Automated) ............................................ 674
5.4.2.4 Ensure root password is set (Automated) .................................................................. 676
5.4.2.5 Ensure root path integrity (Automated) ....................................................................... 678
5.4.2.6 Ensure root user umask is configured (Automated) ................................................... 681
5.4.2.7 Ensure system accounts do not have a valid login shell (Automated) ....................... 684
5.4.2.8 Ensure accounts without a valid login shell are locked (Automated) ......................... 687

**5.4.3 Configure user default environment .................................................................................... 689**

5.4.3.1 Ensure nologin is not listed in /etc/shells (Automated) ............................................... 690
5.4.3.2 Ensure default user shell timeout is configured (Automated) ..................................... 691
5.4.3.3 Ensure default user umask is configured (Automated) .............................................. 695


### 6 Logging and Auditing ...................................................................................................... 702

**6.1 Configure Integrity Checking ..................................................................................................... 703**

6.1.1 Ensure AIDE is installed (Automated) ........................................................................... 704
6.1.2 Ensure filesystem integrity is regularly checked (Automated) ....................................... 706
6.1.3 Ensure cryptographic mechanisms are used to protect the integrity of audit tools
(Automated) ............................................................................................................................ 709

**6.2 System Logging ........................................................................................................................... 712**

Page 7


-----

**6.2.1 Configure journald ................................................................................................................. 713**

**6.2.1.1 Configure systemd-journald service .............................................................................. 714**

6.2.1.1.1 Ensure journald service is enabled and active (Automated) ................................... 715
6.2.1.1.2 Ensure journald log file access is configured (Manual) ........................................... 717
6.2.1.1.3 Ensure journald log file rotation is configured (Manual) .......................................... 719
6.2.1.1.4 Ensure journald ForwardToSyslog is disabled (Automated) ................................... 721
6.2.1.1.5 Ensure journald Storage is configured (Automated)................................................ 725
6.2.1.1.6 Ensure journald Compress is configured (Automated) ............................................ 729

**6.2.1.2 Configure systemd-journal-remote................................................................................. 733**

6.2.1.2.1 Ensure systemd-journal-remote is installed (Automated) ........................................ 734
6.2.1.2.2 Ensure systemd-journal-remote authentication is configured (Manual) .................. 736
6.2.1.2.3 Ensure systemd-journal-upload is enabled and active (Automated) ....................... 738
6.2.1.2.4 Ensure systemd-journal-remote service is not in use (Automated) ......................... 740

**6.2.2 Configure Logfiles.................................................................................................................. 742**

6.2.2.1 Ensure access to all logfiles has been configured (Automated) ................................. 743

**6.4 System Auditing ........................................................................................................................... 749**

**6.4.1 Configure auditd Service ....................................................................................................... 751**

6.4.1.1 Ensure auditd packages are installed (Automated) .................................................... 752
6.4.1.2 Ensure auditd service is enabled and active (Automated) ......................................... 754
6.4.1.3 Ensure auditing for processes that start prior to auditd is enabled (Automated) ....... 756
6.4.1.4 Ensure audit_backlog_limit is sufficient (Automated) ................................................. 758

**6.4.2 Configure Data Retention ...................................................................................................... 760**

6.4.2.1 Ensure audit log storage size is configured (Automated) ........................................... 761
6.4.2.2 Ensure audit logs are not automatically deleted (Automated) .................................... 763
6.4.2.3 Ensure system is disabled when audit logs are full (Automated) ............................... 765
6.4.2.4 Ensure system warns when audit logs are low on space (Automated) ...................... 768

**6.4.3 Configure auditd Rules .......................................................................................................... 771**

6.4.3.1 Ensure changes to system administration scope (sudoers) is collected (Automated)772
6.4.3.2 Ensure actions as another user are always logged (Automated) ............................... 775
6.4.3.3 Ensure events that modify the sudo log file are collected (Automated) ..................... 779
6.4.3.4 Ensure events that modify date and time information are collected (Automated) ...... 783
6.4.3.5 Ensure events that modify the system's network environment are collected
(Automated) ............................................................................................................................ 787
6.4.3.6 Ensure use of privileged commands are collected (Automated) ................................ 791
6.4.3.7 Ensure unsuccessful file access attempts are collected (Automated) ....................... 795
6.4.3.8 Ensure events that modify user/group information are collected (Automated) .......... 799
6.4.3.9 Ensure discretionary access control permission modification events are collected
(Automated) ............................................................................................................................ 803
6.4.3.10 Ensure successful file system mounts are collected (Automated) ........................... 808
6.4.3.11 Ensure session initiation information is collected (Automated) ................................ 812
6.4.3.12 Ensure login and logout events are collected (Automated) ...................................... 816
6.4.3.13 Ensure file deletion events by users are collected (Automated) .............................. 819
6.4.3.14 Ensure events that modify the system's Mandatory Access Controls are collected
(Automated) ............................................................................................................................ 823
6.4.3.15 Ensure successful and unsuccessful attempts to use the chcon command are
recorded (Automated) ............................................................................................................. 826
6.4.3.16 Ensure successful and unsuccessful attempts to use the setfacl command are
recorded (Automated) ............................................................................................................. 830
6.4.3.17 Ensure successful and unsuccessful attempts to use the chacl command are
recorded (Automated) ............................................................................................................. 834
6.4.3.18 Ensure successful and unsuccessful attempts to use the usermod command are
recorded (Automated) ............................................................................................................. 838
6.4.3.19 Ensure kernel module loading unloading and modification is collected (Automated)
................................................................................................................................................ 842
6.4.3.20 Ensure the audit configuration is immutable (Automated) ........................................ 846
6.4.3.21 Ensure the running and on disk configuration is the same (Manual) ....................... 849

Page 8


-----

**6.4.4 Configure auditd File Access ................................................................................................ 851**

6.4.4.1 Ensure audit log files mode is configured (Automated) .............................................. 852
6.4.4.2 Ensure audit log files owner is configured (Automated) ............................................. 855
6.4.4.3 Ensure audit log files group owner is configured (Automated) ................................... 858
6.4.4.4 Ensure the audit log file directory mode is configured (Automated) ........................... 860
6.4.4.5 Ensure audit configuration files mode is configured (Automated) .............................. 863
6.4.4.6 Ensure audit configuration files owner is configured (Automated) ............................. 865
6.4.4.7 Ensure audit configuration files group owner is configured (Automated) ................... 867
6.4.4.8 Ensure audit tools mode is configured (Automated)................................................... 869
6.4.4.9 Ensure audit tools owner is configured (Automated) .................................................. 872
6.4.4.10 Ensure audit tools group owner is configured (Automated) ..................................... 874


### 7 System Maintenance ....................................................................................................... 876

**7.1 System File Permissions ............................................................................................................ 877**

7.1.1 Ensure permissions on /etc/passwd are configured (Automated) ................................. 878
7.1.2 Ensure permissions on /etc/passwd- are configured (Automated) ................................ 880
7.1.3 Ensure permissions on /etc/group are configured (Automated) .................................... 882
7.1.4 Ensure permissions on /etc/group- are configured (Automated) ................................... 884
7.1.5 Ensure permissions on /etc/shadow are configured (Automated) ................................. 886
7.1.6 Ensure permissions on /etc/shadow- are configured (Automated) ................................ 888
7.1.7 Ensure permissions on /etc/gshadow are configured (Automated) ............................... 890
7.1.8 Ensure permissions on /etc/gshadow- are configured (Automated) .............................. 892
7.1.9 Ensure permissions on /etc/shells are configured (Automated) .................................... 894
7.1.10 Ensure permissions on /etc/security/opasswd are configured (Automated) ............... 896
7.1.11 Ensure world writable files and directories are secured (Automated) ......................... 898
7.1.12 Ensure no files or directories without an owner and a group exist (Automated) ......... 902
7.1.13 Ensure SUID and SGID files are reviewed (Manual) ................................................... 905

**7.2 Local User and Group Settings .................................................................................................. 908**

7.2.1 Ensure accounts in /etc/passwd use shadowed passwords (Automated) .................... 909
7.2.2 Ensure /etc/shadow password fields are not empty (Automated) ................................. 912
7.2.3 Ensure all groups in /etc/passwd exist in /etc/group (Automated) ................................. 914
7.2.4 Ensure shadow group is empty (Automated) ................................................................ 916
7.2.5 Ensure no duplicate UIDs exist (Automated) ................................................................. 918
7.2.6 Ensure no duplicate GIDs exist (Automated) ................................................................ 919
7.2.7 Ensure no duplicate user names exist (Automated) ...................................................... 921
7.2.8 Ensure no duplicate group names exist (Automated).................................................... 923
7.2.9 Ensure local interactive user home directories are configured (Automated) ................. 925
7.2.10 Ensure local interactive user dot files access is configured (Automated) ................... 930

## Appendix: Summary Table ....................................................................................... 936

 Appendix: CIS Controls v7 IG 1 Mapped Recommendations ................................ 958

 Appendix: CIS Controls v7 IG 2 Mapped Recommendations ................................ 964

 Appendix: CIS Controls v7 IG 3 Mapped Recommendations ................................ 974

 Appendix: CIS Controls v7 Unmapped Recommendations ................................... 984

 Appendix: CIS Controls v8 IG 1 Mapped Recommendations ................................ 986

 Appendix: CIS Controls v8 IG 2 Mapped Recommendations ................................ 993

 Appendix: CIS Controls v8 IG 3 Mapped Recommendations .............................. 1003

 Appendix: CIS Controls v8 Unmapped Recommendations ................................. 1013

 Appendix: Change History ..................................................................................... 1015

Page 9


-----

