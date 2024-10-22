# (L1) Ensure 'Lock Encrypted Media Extensions' is set to 'Enabled'

## Description

This vulnerability pertains to the automatic download of Encrypted Media Extensions (EME) in Mozilla Firefox without explicit user consent. EME is a JavaScript API used for playing DRM-protected video content in HTML.

The vulnerability arises from the potentially automated download of EME without user interaction. While the default configuration (disabled) does not create an inherent security issue, the absence of required configuration when downloading files is critical for functionality can lead to several risks:

1. **Malware Delivery**: Malicious extensions could potentially install viruses or other harmful software, compromising the user's system.
2. **Privacy Compromise**: Automatically downloaded EME could collect user data or permit another party to do so without user awareness or consent.
3. **Performance Issues**: Unnecessary or malicious extensions can impact browser performance.
4. **Unnecessary Downloads**: Automatic downloads may consume bandwidth, especially on networks with cost or usage limits.

The root cause of this vulnerability lies in the lack of policy enforcement on the automated aspect of EME installation in Firefox. The system lacks a mechanism to mandate explicit user consent for downloading these potentially sensitive components.

## Audit

To audit this setting:

1. Open the Group Policy Management Console (GPMC) on a domain controller or a system with the Group Policy Management tools installed.
2. Navigate to the following UI path:
   ```
   Computer Configuration\Policies\Administrative Templates\Mozilla\Firefox\Encrypted Media Extensions\Lock Encrypted Media Extensions
   ```
3. Verify that the setting is configured as "Enabled".

Alternatively, you can check the registry:

1. Open the Registry Editor (regedit.exe).
2. Navigate to the following registry key:
   ```
   HKLM\SOFTWARE\Policies\Mozilla\Firefox\EncryptedMediaExtensions
   ```
3. Verify that the "Locked" value exists and is set to 1 (REG_DWORD).

## Remediation

To remediate this issue:

### Windows:

1. Download the additional Group Policy template (firefox.admx/adml) from: https://github.com/mozilla/policy-templates/releases
2. Install the template in your Group Policy Central Store or local Policy Definitions folder.
3. Open the Group Policy Management Console (GPMC).
4. Navigate to the appropriate GPO (Domain, OU, or Computer).
5. Edit the GPO and navigate to:
   ```
   Computer Configuration\Policies\Administrative Templates\Mozilla\Firefox\Encrypted Media Extensions\Lock Encrypted Media Extensions
   ```
6. Set the policy to "Enabled".
7. Run `gpupdate /force` on target systems to apply the changes.

### Linux:

For Linux systems running Firefox:

1. Locate the Firefox configuration file, typically found at:
   ```
   /etc/firefox/policies/policies.json
   ```
   If the file doesn't exist, create it.

2. Add or modify the following JSON content:
   ```json
   {
     "policies": {
       "EncryptedMediaExtensions": {
         "Locked": true
       }
     }
   }
   ```

3. Save the file and restart Firefox for the changes to take effect.

Note: Ensure that the file has appropriate permissions (typically owned by root with 644 permissions) to prevent unauthorized modifications.