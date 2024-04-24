# Question

When including a script tag in a HTML page like this, where the script tag is of type module, does all the exported names in the module become accessible in the script?

`<script type="module" src="main.js"><script>`

# Answer

No, the javascript inside the script tag does not get executed. The code in the module does get executed.

## Resources
https://github.com/mdn/js-examples/blob/main/module-examples/basic-modules/index.html
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules