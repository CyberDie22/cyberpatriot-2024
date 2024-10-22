# (L1) Ensure 'Browsing History' is set to 'Disabled'

## Description

This policy setting controls the deletion of user browsing history data upon closing the Mozilla Firefox browser. The recommended state for this setting is: Disabled.

The vulnerability lies not in the browser itself, but in the potential misconfiguration of this setting. While disabling the automatic deletion of browsing history appears to safeguard potentially important data for investigations, it creates a delicate balance between preserving necessary information and protecting user privacy.

**Impact:**
- Forensic investigations may be hindered if essential browsing history is difficult to retrieve or inadvertently lost.
- User privacy may be violated if browsing data persists beyond the current session, potentially conflicting with organizational privacy policies.

## Audit

To audit this setting:

1. Open the Group Policy Management Console (GPMC).
2. Navigate to the following UI path:
   ```
   Computer Configuration\Policies\Administrative Templates\Mozilla\Firefox\Clear data when browser is closed\Browsing History
   ```
3. Verify that the setting is configured as "Disabled".

Alternatively, you can check the registry:

1. Open the Registry Editor.
2. Navigate to the following key:
   ```
   HKLM\SOFTWARE\Policies\Mozilla\Firefox\SanitizeOnShutdown
   ```
3. Verify that the "History" value is set to 0 (REG_DWORD).

## Remediation

To implement the recommended configuration:

### Windows:

1. Open the Group Policy Management Console (GPMC).
2. Create or edit a Group Policy Object (GPO) linked to the appropriate OU.
3. Navigate to the following UI path:
   ```
   Computer Configuration\Policies\Administrative Templates\Mozilla\Firefox\Clear data when browser is closed\Browsing History
   ```
4. Set the policy to "Disabled".

Note: The Firefox ADMX/ADML template is required for this Group Policy setting. You can download it from: https://github.com/mozilla/policy-templates/releases

### Linux:

For Linux systems, Firefox policies are typically managed through a JSON file. To set this policy:

1. Create or edit the file `/etc/firefox/policies/policies.json`.
2. Add or modify the following content:
   ```json
   {
     "policies": {
       "SanitizeOnShutdown": {
         "History": false
       }
     }
   }
   ```
3. Save the file and restart Firefox for the changes to take effect.

Additional considerations:
- Implement complementary policies to safeguard sensitive data after browser closure.
- Develop and enforce data retention policies that balance investigation needs with user privacy.
- Consult legal counsel to ensure compliance with applicable data privacy laws.
- Establish clear data handling procedures for user sessions and investigations.
- Provide employee awareness and training on the implications of this policy.