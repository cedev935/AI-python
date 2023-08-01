# CHANGELOG

## 1.0.1 (2023-08-01)

### Fixes

- Solved an issue that didn't let the user create files with characters such as ',..
- Files could not be overwritten, now a parameter has been added to specify if the files want to be overwritten or not, by default set to True.

---

## 1.0.0 (2023-07-18)

### Improvements

- All charts are based on the same method as free-echarts, making them have a very similar style, and all of them use data sets.

- The free-echarts solution has more possibilities and has a more explicit use.

- State based hierarchical code definition, entering and exiting contexts easily to generate the desired components.

- Easier use of Tabs, Modals and Bentoboxes.

- Tables have been updated to use data sets.

- Charts can use shared data sets, N reports -> 1 data set.

- All the modules use the same interface for referencing resources, a uuid can be passed or a name if possible.

- Caching used resources to minimize API calls.

- Caching can be disabled and enabled.

- Lazy loading of resources (only retrieving resources when needed) to minimize API calls.

- Capacity to reuse resources when possible.

- Clearer output for verbosity options.

- Renaming of resources to clearer names for intuitive use:

- Business -> Workspace

- Dashboard -> Board

- App -> Menu path

- Path -> Sub-path

- Report -> Component

### Removed Functionalities

- Filters have been removed as the behavior is very similar to tabs, in next versions a filter that is applied to data sets will be added.
- Local aggregation of data has been removed as it does not fit well with all solutions with the current data sets.

---

## 0.20.0 (2023-05-10)

This version enables embedding, it's time to share dashboards with the internet!

### Improvements

When creating or updating a dashboard the user can set the parameter is_public to True, this will enable the embedding functionality for the dashboard in the frontal page.

See the updated documentation in:

- [Managing Dashboards](https://docs.shimoku.com/development/advanced-usage/management/managing-dashboards)

---

## 0.19.0 (2023-04-28)

This is a small version that improves the UX of the dashboard manipulation.

### Improvements

- The dashboard's default behaviour on the plotting module has been changed so that the name of the working dashboard is always respected. Before the apps were only included in a dashboard by the plotting module when the apps were being created, now every time an app is used by the plotting module it will check if the app is in the working dashboard, in case it is not, the module will automatically add the app to the dashboard.

- Now the apps can be referenced by name in the dashboards module.

- New methods have been added to the dashboards module:
- `s.dashboard.group_apps`
- `s.dashboard.remove_all_apps_from_dashboard`
- `s.dashboard.is_app_in_dashboard`
- `s.dashboard.force_delete_dashboard`

See the updated documentation in:

- [Quick Start](https://docs.shimoku.com/development/getting-started/quickstart)
- [Menu]
- [Managing Dashboards](https://docs.shimoku.com/development/advanced-usage/management/managing-dashboards)
