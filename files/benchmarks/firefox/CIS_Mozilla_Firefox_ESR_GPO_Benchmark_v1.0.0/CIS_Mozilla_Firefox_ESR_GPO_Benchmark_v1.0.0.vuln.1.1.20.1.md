# (L2) Ensure 'Search Suggestions' is set to 'Disabled'

## Description

This vulnerability relates to a security configuration issue in Mozilla Firefox concerning web search suggestions. The recommended state for this setting is: Disabled.

The vulnerability arises from the fact that user-typed search queries are transmitted to a search engine before the Enter key is pressed. This means that potentially sensitive or unintended data could be exposed to a third-party search engine before the user confirms their request.

Key points:
- Vulnerability Type: Data Exposure/Unintentional Data Leakage (to a third-party search engine)
- Affected System: Mozilla Firefox web browser
- Severity: Medium to Low (depending on the sensitivity of data users might type)
- Impact: Users lose pre-filled search suggestions, but local suggestions remain available

Characters typed by the user are sent to a search engine before the Enter key is pressed, making it possible for unintended data to be sent. This creates a risk of exposing potentially sensitive information to third parties without the user's explicit consent.

## Audit

To audit this setting:

1. For Windows:
   - Open the Registry Editor
   - Navigate to: `HKLM\SOFTWARE\Policies\Mozilla\Firefox`
   - Verify that the `SearchSuggestEnabled` key exists and is set to a REG_DWORD value of 0

2. For Linux:
   - Firefox on Linux typically uses a different configuration method. Check the `policies.json` file in the Firefox installation directory (usually `/etc/firefox/policies/`) for the following content:
     ```json
     {
       "policies": {
         "SearchSuggestEnabled": false
       }
     }
     ```

Additionally, you can verify the setting through the Firefox UI:
1. Open Firefox
2. Navigate to Options/Preferences
3. Go to the Search section
4. Verify that "Provide search suggestions" is unchecked

## Remediation

To remediate this vulnerability:

For Windows:

1. Download the Firefox Group Policy template (firefox.admx/adml) from: https://github.com/mozilla/policy-templates/releases
2. Install the template in your Group Policy Central Store or local Policy Definitions folder
3. Open the Group Policy Management Console
4. Navigate to: Computer Configuration > Policies > Administrative Templates > Mozilla > Firefox > Search
5. Set the "Search Suggestions" policy to Disabled

Alternatively, you can set the registry key directly:
1. Open the Registry Editor
2. Navigate to: `HKLM\SOFTWARE\Policies\Mozilla\Firefox`
3. Create a new DWORD value named `SearchSuggestEnabled`
4. Set its value to 0

For Linux:

1. Create or edit the file `/etc/firefox/policies/policies.json`
2. Ensure it contains the following content:
   ```json
   {
     "policies": {
       "SearchSuggestEnabled": false
     }
   }
   ```
3. Save the file and restart Firefox

For both platforms, it's recommended to also educate users about the potential risks of entering sensitive information in search engines, particularly without confirming their intentions. Implement security awareness training to help users better understand the privacy implications of using web search suggestions and other features that pre-emptively submit user input.