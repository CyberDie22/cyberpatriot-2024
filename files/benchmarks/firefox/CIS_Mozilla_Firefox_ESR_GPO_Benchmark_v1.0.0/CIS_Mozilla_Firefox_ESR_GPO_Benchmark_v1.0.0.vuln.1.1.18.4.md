# (L1) Ensure 'dom.allow_scripts_to_close_windows' is set to 'Disabled'

## Description

The `dom.allow_scripts_to_close_windows` setting in Mozilla Firefox controls whether scripts can close browser windows. When enabled, this setting allows websites to use JavaScript to close browser windows, potentially without user consent or intention. This can lead to several security risks:

1. **Data Loss**: Users might lose unsaved work or progress in the affected window.
2. **Session Hijacking**: An attacker could make the attack window seem like a legitimate interaction, potentially compromising user sessions.
3. **Malicious Redirect**: Closing the original window might be part of a redirect to a phishing site or a malicious website.

The recommended state for this setting is: Disabled.

Disabling this setting prevents scripts from arbitrarily closing browser windows, reducing the probability of a user losing work or state being performed in another tab within the same window.

## Audit

To audit this setting:

1. Navigate to the following registry location:
   ```
   HKLM\SOFTWARE\Policies\Mozilla\Firefox\Preferences
   ```
2. Verify that the `dom.allow_scripts_to_close_windows` value is set to `0` (REG_DWORD).

Alternatively, you can check the Group Policy setting:

1. Open the Group Policy Management Console.
2. Navigate to the following UI path:
   ```
   Computer Configuration\Policies\Administrative Templates\Mozilla\Firefox\Preferences (Deprecated)\dom.allow_scripts_to_close_windows
   ```
3. Confirm that it is set to "Disabled".

## Remediation

To implement the recommended configuration:

1. Download and install the additional Group Policy template (firefox.admx/adml) from:
   https://github.com/mozilla/policy-templates/releases

2. Open the Group Policy Management Console.

3. Navigate to the following UI path:
   ```
   Computer Configuration\Policies\Administrative Templates\Mozilla\Firefox\Preferences (Deprecated)\dom.allow_scripts_to_close_windows
   ```

4. Set the policy to "Disabled".

5. Apply the Group Policy changes.

This will create the following registry entry:
```
HKLM\SOFTWARE\Policies\Mozilla\Firefox\Preferences
dom.allow_scripts_to_close_windows = 0 (REG_DWORD)
```