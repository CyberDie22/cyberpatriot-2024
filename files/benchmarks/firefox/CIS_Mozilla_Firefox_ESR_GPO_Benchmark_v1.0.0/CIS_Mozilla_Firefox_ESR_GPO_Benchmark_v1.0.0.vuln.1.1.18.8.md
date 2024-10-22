# (L1) Ensure 'media.peerconnection.enabled' is set to 'Disabled'

## Description

This policy setting determines whether Web Real Time Communications (WebRTC) is allowed in Mozilla Firefox. WebRTC is used for peer-to-peer communication such as file sharing or video calls. The recommended state for this setting is: Disabled.

WebRTC can expose private information such as internal IP addresses and computer settings. By disabling this feature, you can prevent potential information leakage and enhance the overall security posture of the system.

However, it's important to note that disabling WebRTC may impact functionality for applications that rely on this technology. Organizations should carefully consider their use cases and potential alternatives before implementing this policy.

## Audit

To audit this setting, follow these steps:

### Windows:

1. Open the Registry Editor (regedit.exe)
2. Navigate to the following registry key:
   ```
   HKLM\SOFTWARE\Policies\Mozilla\Firefox\Preferences
   ```
3. Verify that the `media.peerconnection.enabled` value exists and is set to `0` (REG_DWORD)

### Linux:

1. Check the Firefox configuration file (usually located at `/etc/firefox/policies/policies.json`)
2. Look for the following entry:
   ```json
   {
     "policies": {
       "Preferences": {
         "media.peerconnection.enabled": false
       }
     }
   }
   ```

## Remediation

To remediate this issue, follow these steps:

### Windows:

1. Open the Group Policy Management Console
2. Navigate to: Computer Configuration > Policies > Administrative Templates > Mozilla > Firefox > Preferences (Deprecated)
3. Locate and double-click on the "media.peerconnection.enabled" policy
4. Set it to "Disabled"
5. Click "Apply" and then "OK"

Note: This Group Policy path may not exist by default. You may need to download and install an additional Group Policy template (firefox.admx/adml) from Mozilla's official website.

### Linux:

1. Open or create the Firefox configuration file (usually located at `/etc/firefox/policies/policies.json`)
2. Add or modify the following content:
   ```json
   {
     "policies": {
       "Preferences": {
         "media.peerconnection.enabled": false
       }
     }
   }
   ```
3. Save the file and restart Firefox for the changes to take effect

Remember to test the configuration thoroughly after implementation to ensure that critical business functions are not impacted by this change.