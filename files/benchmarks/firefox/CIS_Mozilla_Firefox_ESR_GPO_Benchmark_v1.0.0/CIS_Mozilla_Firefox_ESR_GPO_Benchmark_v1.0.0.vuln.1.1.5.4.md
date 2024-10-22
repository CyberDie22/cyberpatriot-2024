## Description

The "Form & Search History" setting in Mozilla Firefox allows for the deletion of user data upon closing the browser. This setting, when enabled, can potentially impair forensic investigations by deleting critical information recorded in browsing history or form data. The recommended state for this setting is: Disabled.

While this is not a vulnerability in the traditional sense of an exploitable flaw, it represents a configuration error that can lead to the loss of valuable data for forensic analysis. The potential impact is a loss of critical evidence during a computer forensic investigation, which could affect investigations ranging from simple troubleshooting to more serious security breaches.

The root cause of this issue is not a technical flaw in Firefox, but rather a misconfiguration of a Group Policy setting (or analogous configuration tool). This policy, designed to protect user privacy, can be counterproductive if not understood and appropriately applied.

It's crucial to consider:
1. Organizational Policy Compliance: Preserving this data might contradict organizational policies regarding user privacy.
2. Forensic Implications: The policy should align with the potential need to preserve data for forensic investigations.
3. User Privacy vs. Security: A balance must be struck between user privacy and security needs.

## Audit

To audit this setting:

1. Navigate to the following UI path:
   ```
   Computer Configuration\Policies\Administrative Templates\Mozilla\Firefox\Clear data when browser is closed\Form & Search History
   ```
2. Confirm that it is set to "Disabled".

Alternatively, you can check the following registry location:

```
HKLM\SOFTWARE\Policies\Mozilla\Firefox\SanitizeOnShutdown:FormData
```

The REG_DWORD value should be 0.

## Remediation

To establish the recommended configuration:

### Windows:

1. Open the Group Policy Management Console (GPMC) or Local Group Policy Editor.
2. Navigate to the following UI path:
   ```
   Computer Configuration\Policies\Administrative Templates\Mozilla\Firefox\Clear data when browser is closed\Form & Search History
   ```
3. Set the policy to "Disabled".

### Linux:

For Linux systems, Firefox typically doesn't use Group Policy. Instead, you can configure this setting through the `policies.json` file:

1. Create or edit the file `/etc/firefox/policies/policies.json` (for system-wide settings) or `~/.mozilla/firefox/<profile>/policies.json` (for user-specific settings).
2. Add or modify the following JSON:
   ```json
   {
     "policies": {
       "SanitizeOnShutdown": {
         "FormData": false
       }
     }
   }
   ```
3. Save the file and restart Firefox for the changes to take effect.

Remember to align this configuration with your organization's specific needs and policies regarding data retention and privacy.