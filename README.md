# Mary Jane Files

Separate offline Android record organizer. Uploaded bookshelf banner is included in `assets/bookshelf.jpg`.

## Build APK

1. Create a new GitHub repository named `mary-jane-files` and upload this project's files (including `.github/workflows/android.yml`). Do not use the Sugarcane Ledger repository.
2. In Expo, create a new EAS project: `npm install`, `npx eas-cli login`, `npx eas-cli init` (this updates `app.json` with the project ID).
3. For a first build, run `npx eas-cli build --platform android --profile preview` in a terminal. Follow prompts to configure Android signing credentials.
4. When the build completes, Expo provides an APK download link.

GitHub Actions workflow is provided as an optional automated build after configuring repository secret `EXPO_TOKEN` and the EAS project ID. It runs `eas build --non-interactive --no-wait`; initial Android credentials should be configured in the first interactive build.

All folders and records are stored on the device using AsyncStorage. Uninstalling or clearing app data can erase them; export/backup is not implemented yet. Ages update based on the device's current date. Folder deletion removes its records after confirmation.
