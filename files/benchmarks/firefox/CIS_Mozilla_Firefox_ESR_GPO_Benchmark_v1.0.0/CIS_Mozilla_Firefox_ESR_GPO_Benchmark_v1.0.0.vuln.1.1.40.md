# (L2) Ensure 'New Tab Page' is set to 'Disabled'

## Description

The "New Tab Page" feature in Mozilla Firefox displays a list of built-in top sites and frequently visited websites by default. This can potentially expose sensitive information from the user's browsing history. The recommended state for this setting is: Disabled.

When enabled, the New Tab Page aggregates and displays the user's browsing history, including frequently visited sites. This can lead to inadvertent disclosure of sensitive information such as login pages, financial accounts, and other personal data. The vulnerability lies in the default configuration, which does not control or limit this data collection and display, potentially compromising user privacy.

It's important to note that this vulnerability is a configuration issue and does not require active exploitation. Simply not disabling the New Tab Page feature is the vulnerability itself.

## Audit

To audit this setting:

1. Open the Group Policy Management Editor.
2. Navigate to the following path:
   `Computer Configuration\Policies\Administrative Templates\Mozilla\Firefox\New Tab Page`
3. Verify that the setting is set to "Disabled".

Alternatively, you can check the registry:

1. Open the Registry Editor.
2. Navigate to the following key:
   `HKLM\SOFTWARE\Policies\Mozilla\Firefox`
3. Verify that the "NewTabPage" value exists and is set to 0 (REG_DWORD).

```
HKLM\SOFTWARE\Policies\Mozilla\Firefox:NewTabPage = 0
```

## Remediation

### Windows:

To establish the recommended configuration via Group Policy:

1. Ensure you have the necessary Firefox Group Policy template (firefox.admx/adml). If not, download it from: https://github.com/mozilla/policy-templates/releases
2. Open the Group Policy Management Editor.
3. Navigate to the following path:
   `Computer Configuration\Policies\Administrative Templates\Mozilla\Firefox\New Tab Page`
4. Set the policy to "Disabled".
5. Apply the changes and update group policy on target systems (gpupdate /force).

### Linux:

For Linux systems, Firefox policies are typically managed through a JSON file. To disable the New Tab Page:

1. Create or edit the file `/etc/firefox/policies/policies.json`
2. Add or modify the following content:

```json
{
  "policies": {
    "NewTabPage": false
  }
}
```

3. Save the file and restart Firefox for the changes to take effect.

Note: Ensure that the file and directory have appropriate permissions for the Firefox process to read them.