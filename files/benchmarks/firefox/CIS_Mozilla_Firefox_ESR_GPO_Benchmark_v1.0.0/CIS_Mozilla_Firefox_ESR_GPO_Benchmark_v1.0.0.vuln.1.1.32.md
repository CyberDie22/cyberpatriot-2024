# (L1) Ensure 'Disable Pocket' is set to 'Enabled'

## Description

Pocket, previously known as Read It Later, is a social bookmark service integrated into Mozilla Firefox. It allows users to save various types of content (web pages, blogs, videos, news sources) to access later from any device. The recommended state for the 'Disable Pocket' setting is: Enabled.

This configuration issue doesn't represent a security vulnerability in Firefox itself, but rather a misconfiguration that prevents the use of the Pocket feature. The problem arises from a missing or incorrectly configured group policy setting.

When the 'Disable Pocket' policy is enabled (default value), it prevents Firefox from accessing and using the Pocket service. The correct configuration is to disable this policy by setting it to "Enabled," which counterintuitively enables the Pocket functionality.

It's important to note that using Pocket involves agreeing to let Firefox collect information about browser and device type. This information, along with other data related to Pocket user accounts, may be shared with third parties. Additionally, Firefox may request usernames and passwords for third-party sites to access articles and information published on them.

## Audit

To audit this setting:

### Windows:

1. Open the Group Policy Editor.
2. Navigate to Computer Configuration > Policies > Administrative Templates > Mozilla > Firefox
3. Locate the "Disable Pocket" setting.
4. Verify that it is set to "Enabled".

Alternatively, you can check the registry:

1. Open the Registry Editor.
2. Navigate to HKLM\SOFTWARE\Policies\Mozilla\Firefox
3. Verify that the "DisablePocket" key exists and has a REG_DWORD value of 1.

### Linux:

Firefox policies on Linux are typically managed through a JSON file. To audit:

1. Check for the existence of the policy file:
   ```
   ls /usr/lib/firefox/distribution/policies.json
   ```
2. If the file exists, examine its contents:
   ```
   cat /usr/lib/firefox/distribution/policies.json
   ```
3. Look for a "DisablePocket" entry set to false, which enables the Pocket feature:
   ```json
   {
     "policies": {
       "DisablePocket": false
     }
   }
   ```

## Remediation

To remediate this issue:

### Windows:

1. Download and install the Firefox Group Policy template (firefox.admx/adml) if not already present.
2. Open the Group Policy Editor.
3. Navigate to Computer Configuration > Policies > Administrative Templates > Mozilla > Firefox
4. Locate and double-click on "Disable Pocket".
5. Set it to "Enabled".
6. Click "Apply" and then "OK".

### Linux:

1. Create or edit the Firefox policy file:
   ```
   sudo nano /usr/lib/firefox/distribution/policies.json
   ```
2. Ensure the file contains the following content:
   ```json
   {
     "policies": {
       "DisablePocket": false
     }
   }
   ```
3. Save the file and exit the editor.
4. Restart Firefox for the changes to take effect.

Note: Setting "DisablePocket" to false in the policy file enables the Pocket feature, which is the desired configuration despite the counterintuitive naming.