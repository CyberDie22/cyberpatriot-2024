# (L1) Ensure 'Extension Recommendations' is set to 'Disabled'

## Description

This vulnerability involves a configuration issue in Mozilla Firefox concerning extension recommendations. When enabled, this setting allows Firefox to send user data to third-party extension recommendation services, potentially exposing sensitive information about the user's browsing habits and interests.

Key points:
- Vulnerability Type: Configuration weakness (not a software bug)
- Affected Software: Mozilla Firefox (Group Policy configuration)
- Impact: Potential exposure of user browsing data to third-party services
- Severity: High to critical, especially for privacy-sensitive users or organizations

The vulnerability stems from an uncontrolled data transmission that occurs when extension recommendations are enabled. While not exploitable in the traditional sense, it poses a significant privacy risk through the passive transmission of user data.

## Audit

To audit this setting:

1. Open the Group Policy Management Console (GPMC)
2. Navigate to the following UI path:
   ```
   Computer Configuration\Policies\Administrative Templates\Mozilla\Firefox\UserMessaging\Extension Recommendations
   ```
3. Verify that the setting is configured as "Disabled"

Alternatively, you can check the registry:

1. Open the Registry Editor
2. Navigate to the following key:
   ```
   HKLM\SOFTWARE\Policies\Mozilla\Firefox\UserMessaging
   ```
3. Verify that the "ExtensionRecommendations" value is set to "0" (REG_DWORD)

Note: If the policy path or registry key doesn't exist, it may indicate that the required ADMX/ADML template has not been properly installed.

## Remediation

### Windows:

1. Download the latest Firefox ADMX/ADML template from: https://github.com/mozilla/policy-templates/releases
2. Copy the downloaded .admx file to `C:\Windows\PolicyDefinitions`
3. Copy the downloaded .adml file to `C:\Windows\PolicyDefinitions\en-US` (or the appropriate language folder)
4. Open the Group Policy Management Console (GPMC)
5. Navigate to:
   ```
   Computer Configuration\Policies\Administrative Templates\Mozilla\Firefox\UserMessaging\Extension Recommendations
   ```
6. Set the policy to "Disabled"
7. Run `gpupdate /force` from an elevated command prompt to apply the changes

### Linux:

Firefox on Linux typically doesn't use Group Policy. Instead, you can disable extension recommendations by:

1. Open a text editor with root privileges
2. Create or edit the file `/etc/firefox/policies/policies.json`
3. Add or modify the following content:
   ```json
   {
     "policies": {
       "ExtensionRecommendations": false
     }
   }
   ```
4. Save the file and restart Firefox

Remember to educate users about the privacy implications of enabling extension recommendations and enforce this policy across all managed Firefox installations.