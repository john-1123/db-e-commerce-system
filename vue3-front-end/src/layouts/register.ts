import { ModuleNamespace } from 'vite/types/hot';
import { App } from 'vue';

/**
 * Register layouts in the app instance
 *
 * @param {App<Element>} app
 */
export function registerLayouts(app: App<Element>) {
  const layouts = import.meta.globEager<string, ModuleNamespace>('./*.vue');

  Object.entries(layouts).forEach(([, layout]) => {
    app.component(layout?.default?.name, layout?.default);
  });
}
