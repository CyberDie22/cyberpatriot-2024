# (L1) Ensure 'Active Logins' is set to 'Disabled'

## Description

This policy setting allows for the user session to be cleared upon closing the browser. The recommended state for this setting is: Disabled.

Deleting browser data will delete information that may be important for a computer investigation. Computer Forensics Analysts may not be able to retrieve pertinent information for an investigation if this setting is enabled.

When the "Active Logins" setting in Mozilla Firefox is set to "Disabled", it prevents the automatic clearing of active sessions. This preserves user session data, including login credentials, browsing history, and stored passwords, which can be crucial for forensic investigations.

While not inherently a vulnerability, this configuration impacts the security posture regarding data preservation and potential forensics investigations. The absence or insufficient management of this data could be considered an oversight that could impact an investigation.

## Audit

To audit this setting:

1. Open the Group Policy Management Console (GPMC) on a domain controller or a system with the Group Policy Management tools installed.

2. Navigate to the following UI path:
   ```
   Computer Configuration\Policies\Administrative Templates\Mozilla\Firefox\Clear data when browser is closed\Active Logins
   ```

3. Verify that the setting is configured as "Disabled".

4. Additionally, you can check the registry to confirm the setting:

   For Windows:
   1. Open the Registry Editor (regedit.exe)
   2. Navigate to the following key:
      ```
      HKLM\SOFTWARE\Policies\Mozilla\Firefox\SanitizeOnShutdown
      ```
   3. Verify that the "Sessions" value is set to 0 (REG_DWORD)

   For Linux:
   1. Check the Firefox configuration file (usually located in ~/.mozilla/firefox/[profile]/prefs.js)
   2. Look for the following line:
      ```
      user_pref("privacy.clearOnShutdown.sessions", false);
      ```

## Remediation

To implement the recommended configuration:

For Windows:
1. Open the Group Policy Management Console (GPMC)
2. Create a new Group Policy Object or edit an existing one
3. Navigate to the following path:
   ```
   Computer Configuration\Policies\Administrative Templates\Mozilla\Firefox\Clear data when browser is closed\Active Logins
   ```
4. Set the policy to "Disabled"
5. Apply the Group Policy to the relevant Organizational Units (OUs)

Note: This Group Policy path may not exist by default. You may need to download and install an additional Group Policy template (firefox.admx/adml) from Mozilla.

For Linux:
1. Locate the Firefox configuration file (usually in ~/.mozilla/firefox/[profile]/prefs.js)
2. Add or modify the following line:
   ```
   user_pref("privacy.clearOnShutdown.sessions", false);
   ```
3. Save the file and restart Firefox

For both Windows and Linux, ensure that your organization's security policies and procedures are updated to reflect this configuration change, and that proper data retention and forensic procedures are in place to make use of the preserved session data when necessary.