# Table of Contents

#### Terms of Use ................................................................................................................. 1

 Table of Contents .......................................................................................................... 2

 Overview ........................................................................................................................ 5

##### Intended Audience ................................................................................................................. 5

 Consensus Guidance ............................................................................................................ 6

 Typographical Conventions .................................................................................................. 7

#### Recommendation Definitions ....................................................................................... 8

##### Title ......................................................................................................................................... 8

 Assessment Status ................................................................................................................ 8

**Automated .............................................................................................................................................. 8**
**Manual ..................................................................................................................................................... 8**

##### Profile ..................................................................................................................................... 8

 Description ............................................................................................................................. 8

 Rationale Statement .............................................................................................................. 8

 Impact Statement ................................................................................................................... 9

 Audit Procedure ..................................................................................................................... 9

 Remediation Procedure ......................................................................................................... 9

 Default Value .......................................................................................................................... 9

 References ............................................................................................................................. 9

 CIS Critical Security Controls[®] (CIS Controls[®]) ................................................................... 9

 Additional Information........................................................................................................... 9

 Profile Definitions .................................................................................................................10

 Acknowledgements ..............................................................................................................11

#### Recommendations ...................................................................................................... 12

##### 1 Mozilla ................................................................................................................................12

**1.1 Firefox ............................................................................................................................................. 12**

**1.1.1 Addons ...................................................................................................................................... 12**

1.1.1.1 (L1) Ensure 'Allow add-on installs from websites' is set to 'Disabled' (Automated) ..... 13

**1.1.2 Authentication .......................................................................................................................... 15**

1.1.2.1 (L1) Ensure 'NTLM' is set to 'Disabled' (Automated) .................................................... 16

**1.1.3 Bookmarks ................................................................................................................................ 18**
**1.1.4 Certificates ................................................................................................................................ 18**
**1.1.5 Clear data when browser is closed ........................................................................................ 18**

1.1.5.1 (L1) Ensure 'Active Logins’ is set to ‘Disabled’ (Automated) ........................................ 19
1.1.5.2 (L1) Ensure 'Browsing History' is set to 'Disabled' (Automated) ................................... 21
1.1.5.3 (L1) Ensure 'Download History' is set to 'Disabled' (Automated) ................................. 23
1.1.5.4 (L1) Ensure 'Form & Search History' is set to 'Disabled' (Automated) ......................... 25


Page 2


-----

1.1.5.5 (L1) Ensure 'Locked' is set to 'Enabled' (Automated) ................................................... 27

**1.1.6 Cookies ..................................................................................................................................... 29**

1.1.6.1 (L1) Ensure 'Cookie Behavior' is set to 'Enabled: Reject cookies for known trackers
and partition third-party cookies' (Automated) .......................................................................... 30
1.1.6.2 (L1) Ensure 'Cookie Behavior in private browsing' is set to 'Enabled: Reject cookies for
known trackers and partition third-party cookies' (Automated) ................................................. 32

**1.1.7 Disabled Ciphers ...................................................................................................................... 34**

1.1.7.1 (L1) Ensure 'TLS_RSA_WITH_3DES_EDE_CBC_SHA ' is set to 'Enabled'
(Automated) .............................................................................................................................. 35

**1.1.8 DNS Over HTTPS ...................................................................................................................... 37**
**1.1.9 Encrypted Media Extensions .................................................................................................. 37**

1.1.9.1 (L1) Ensure 'Lock Encrypted Media Extensions’ is set to ‘Enabled’ (Automated) ........ 38

**1.1.10 Extensions .............................................................................................................................. 40**

1.1.10.1 (L1) Ensure 'Extension Update' is set to 'Enabled' (Automated) ................................ 41

**1.1.11 Firefox Suggest (US only) ..................................................................................................... 43**
**1.1.12 Flash ........................................................................................................................................ 43**

1.1.12.1 (L1) Ensure 'Activate Flash on websites' is set to 'Disabled' (Automated) ................. 44

**1.1.13 Home page .............................................................................................................................. 46**
**1.1.14 PDF.js ...................................................................................................................................... 46**
**1.1.15 Permissions ............................................................................................................................ 46**
**1.1.15.1 Autoplay ............................................................................................................................... 46**
**1.1.15.2 Camera ................................................................................................................................. 46**

**1.1.15.3 Location ............................................................................................................................. 46**

1.1.15.1.1 (L1) Ensure 'Block new requests asking to access location' is set to 'Enabled'
(Automated) .............................................................................................................................. 48
1.1.15.1.2 (L1) Ensure 'Do not allow preferences to be changed' is set to 'Enabled'
(Automated) .............................................................................................................................. 50

**1.1.16 Picture-in-Picture ................................................................................................................... 52**
**1.1.17 Popups .................................................................................................................................... 52**

1.1.17.1 (L1) Ensure 'Block pop-ups from websites' is set to 'Enabled' (Automated) .............. 53
1.1.17.2 (L1) Ensure 'Do not allow preferences to be changed' is set to 'Enabled' (Automated)
.................................................................................................................................................. 55

**1.1.18 Preferences (Deprecated) ...................................................................................................... 57**

1.1.18.1 (L1) Ensure 'browser.safebrowsing.malware.enabled' is set to 'Enabled' (Automated)
.................................................................................................................................................. 58
1.1.18.2 (L1) Ensure 'browser.safebrowsing.phishing.enabled' is set to 'Enabled' (Automated)
.................................................................................................................................................. 60
1.1.18.3 (L1) Ensure 'browser.search.update' is set to 'Enabled' (Automated) ........................ 62
1.1.18.4 (L1) Ensure 'dom.allow_scripts_to_close_windows' is set to 'Disabled' (Automated) 64
1.1.18.5 (L1) Ensure 'dom.disable_window_flip' is set to 'Enabled' (Automated) .................... 66
1.1.18.6 (L1) Ensure 'dom.disable_window_move_resize' is set to 'Enabled' (Automated) .... 68
1.1.18.7 (L1) Ensure 'extensions.blocklist.enabled' is set to 'Enabled' (Automated) ............... 70
1.1.18.8 (L1) Ensure 'media.peerconnection.enabled' is set to 'Disabled' (Automated) .......... 72
1.1.18.9 (L2) Ensure 'network.IDN_show_punycode' is set to 'Enabled' (Automated) ............ 74
1.1.18.10 (L1) Ensure 'security.mixed_content.block_active_content' is set to 'Enabled'
(Automated) .............................................................................................................................. 76

**1.1.19 Proxy Settings ........................................................................................................................ 78**

1.1.19.1 (L1) Ensure 'Connection Type' is set to 'Enabled: No Proxy' (Automated) ................ 79
1.1.19.2 (L1) Ensure 'Do not allow proxy settings to be changed' is set to 'Enabled'
(Automated) .............................................................................................................................. 81

**1.1.20 Search ..................................................................................................................................... 83**

1.1.20.1 (L2) Ensure 'Search Suggestions' is set to 'Disabled' (Automated) ........................... 84

**1.1.21 Security Devices..................................................................................................................... 86**
**1.1.22 Tracking Protection ............................................................................................................... 86**

1.1.22.1 (L1) Ensure 'Cryptomining' is set to 'Enabled' (Automated) ....................................... 87

Page 3


-----

1.1.22.2 (L1) Ensure 'Do not allow tracking protection preferences to be changed' is set to
'Enabled' (Automated) ............................................................................................................... 89
1.1.22.3 (L1) Ensure 'Email Tracking' is set to 'Enabled' (Automated) ..................................... 91
1.1.22.4 (L1) Ensure 'Enabled' is set to 'Enabled' (Automated) ............................................... 93
1.1.22.5 (L1) Ensure 'Fingerprinting' is set to 'Enabled' (Automated) ...................................... 95

**1.1.23 User Messaging ...................................................................................................................... 97**

1.1.23.1 (L1) Ensure 'Extension Recommendations' is set to 'Disabled' (Automated) ............. 98
1.1.24 (L1) Ensure 'Application Autoupdate' is set to 'Enabled' (Automated) ........................ 100
1.1.25 (L1) Ensure 'Background updater' is set to 'Enabled' (Automated) ............................. 102
1.1.26 (L1) Ensure 'Disable Developer Tools' is set to 'Enabled' (Automated) ...................... 104
1.1.27 (L1) Ensure 'Disable Feedback Commands' is set to 'Enabled' (Automated) ............. 106
1.1.28 (L1) Ensure 'Disable Firefox Accounts' is set to 'Enabled' (Automated) ...................... 108
1.1.29 (L1) Ensure 'Disable Firefox Studies' is set to 'Enabled' (Automated) ........................ 110
1.1.30 (L1) Ensure 'Disable Forget Button' is set to 'Enabled' (Automated) ........................... 112
1.1.31 (L2) Ensure 'Disable Form History' is set to 'Enabled' (Automated) ............................ 113
1.1.32 (L1) Ensure 'Disable Pocket' is set to 'Enabled' (Automated) ..................................... 115
1.1.33 (L1) Ensure 'Disable Private Browsing' is set to 'Enabled' (Automated) ..................... 117
1.1.34 (L1) Ensure 'Disable System Addon Updates' is set to 'Disabled' (Automated) .......... 119
1.1.35 (L1) Ensure 'Disable Telemetry' is set to 'Enabled' (Automated) ................................ 121
1.1.36 (L1) Ensure 'Disable Update' is set to 'Disabled' (Automated) .................................... 123
1.1.37 (L1) Ensure 'Maximum SSL version enabled' is set to 'Enabled: TLS 1.3' (Automated)
................................................................................................................................................ 125
1.1.38 (L1) Ensure 'Minimum SSL version enabled' is set to 'Enabled: TLS 1.2' (Automated)
................................................................................................................................................ 127
1.1.39 (L1) Ensure 'Network Prediction' is set to 'Disabled' (Automated) .............................. 129
1.1.40 (L2) Ensure 'New Tab Page' is set to 'Disabled' (Automated) ..................................... 131
1.1.41 (L1) Ensure 'Offer to save logins' is set to 'Disabled' (Automated) .............................. 133
1.1.42 (L1) Ensure 'Password Manager' is set to 'Disabled' (Automated) .............................. 135

#### Appendix: Summary Table ....................................................................................... 137

 Appendix: Change History ....................................................................................... 143

Page 4


-----

# Overview

#### All CIS Benchmarks™ focus on technical configuration settings used to maintain and/or increase the security of the addressed technology, and they should be used in conjunction with other essential cyber hygiene tasks like:

 • Monitoring the base operating system for vulnerabilities and quickly updating with
 the latest security patches. 

 • Monitoring applications and libraries for vulnerabilities and quickly updating with
 the latest security patches.

 In the end, the CIS Benchmarks are designed as a key component of a comprehensive cybersecurity program. 

 This document provides prescriptive guidance for establishing a secure configuration posture for the Mozilla Firefox ESR Browser. This guide was tested against Mozilla Firefox 115.10 ESR on a Windows 11 Release 23H2 operating system. To obtain the latest version of this guide, please visit http://benchmarks.cisecurity.org. If you have questions, comments, or have identified ways to improve this guide, please write us at feedback@cisecurity.org.

## Intended Audience

#### This benchmark is intended for system and application administrators, security specialists, auditors, help desk, and platform deployment personnel who plan to develop, deploy, assess, or secure solutions that incorporate the Mozilla Firefox ESR Browser via Group Policy Objects (GPOs).

Page 5


-----

## Consensus Guidance

#### This CIS Benchmark™ was created using a consensus review process comprised of a global community of subject matter experts. The process combines real world experience with data-based information to create technology specific guidance to assist users to secure their environments. Consensus participants provide perspective from a diverse set of backgrounds including consulting, software development, audit and compliance, security research, operations, government, and legal. 

 Each CIS Benchmark undergoes two phases of consensus review. The first phase occurs during initial Benchmark development. During this phase, subject matter experts convene to discuss, create, and test working drafts of the Benchmark. This discussion occurs until consensus has been reached on Benchmark recommendations. The second phase begins after the Benchmark has been published. During this phase, all feedback provided by the Internet community is reviewed by the consensus team for incorporation in the Benchmark. If you are interested in participating in the consensus process, please visit https://workbench.cisecurity.org/.

Page 6


-----

## Typographical Conventions

#### The following typographical conventions are used throughout this guide:

|Convention|Meaning|
|---|---|
|Stylized Monospace font|Used for blocks of code, command, and script examples. Text should be interpreted exactly as presented.|
|Monospace font|Used for inline code, commands, UI/Menu selections or examples. Text should be interpreted exactly as presented.|
|<Monospace font in brackets>|Text set in angle brackets denote a variable requiring substitution for a real value.|
|Italic font|Used to reference other relevant settings, CIS Benchmarks and/or Benchmark Communities. Also, used to denote the title of a book, article, or other publication.|
|Bold font|Additional information or caveats things like Notes, Warnings, or Cautions (usually just the word itself and the rest of the text normal).|


Page 7


-----

# Recommendation Definitions

#### The following defines the various components included in a CIS recommendation as applicable. If any of the components are not applicable it will be noted or the component will not be included in the recommendation.  

## Title

#### Concise description for the recommendation's intended configuration. 

## Assessment Status

#### An assessment status is included for every recommendation. The assessment status indicates whether the given recommendation can be automated or requires manual steps to implement. Both statuses are equally important and are determined and supported as defined below: 

### Automated

#### Represents recommendations for which assessment of a technical control can be fully automated and validated to a pass/fail state. Recommendations will include the necessary information to implement automation.

### Manual

#### Represents recommendations for which assessment of a technical control cannot be fully automated and requires all or some manual steps to validate that the configured state is set as expected. The expected state can vary depending on the environment.

## Profile

#### A collection of recommendations for securing a technology or a supporting platform. Most benchmarks include at least a Level 1 and Level 2 Profile. Level 2 extends Level 1 recommendations and is not a standalone profile. The Profile Definitions section in the benchmark provides the definitions as they pertain to the recommendations included for the technology. 

## Description

#### Detailed information pertaining to the setting with which the recommendation is concerned. In some cases, the description will include the recommended value.

## Rationale Statement

#### Detailed reasoning for the recommendation to provide the user a clear and concise understanding on the importance of the recommendation.

Page 8


-----

## Impact Statement 

#### Any security, functionality, or operational consequences that can result from following the recommendation.

## Audit Procedure 

#### Systematic instructions for determining if the target system complies with the recommendation.

## Remediation Procedure

#### Systematic instructions for applying recommendations to the target system to bring it into compliance according to the recommendation.

## Default Value

#### Default value for the given setting in this recommendation, if known. If not known, either not configured or not defined will be applied. 

## References

#### Additional documentation relative to the recommendation. 

## CIS Critical Security Controls[®] (CIS Controls[®])

#### The mapping between a recommendation and the CIS Controls is organized by CIS Controls version, Safeguard, and Implementation Group (IG). The Benchmark in its entirety addresses the CIS Controls safeguards of (v7) “5.1 - Establish Secure Configurations” and (v8) '4.1 - Establish and Maintain a Secure Configuration Process” so individual recommendations will not be mapped to these safeguards.

## Additional Information 

#### Supplementary information that does not correspond to any other field but may be useful to the user. 

Page 9


-----

