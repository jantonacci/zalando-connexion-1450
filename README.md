### Description
Using Relative URLs in OAS `info` raises multiple js `TypeError: Failed to construct 'URL': Invalid base URL" exceptions in Swagger UI:
1. system.js:490 on page load
2. url.js:15 on Authorization

### Expected behaviour
Per https://swagger.io/docs/specification/api-host-and-base-path/ section Relative URLs, using a (valid) relative URL is permitted.  

### Actual behaviour
Swagger UI page loads w/o any obvious issues.  Swagger UI Authorize button does not respond.

_Swagger UI (page load)_
```java
system.js:490 TypeError: Failed to construct 'URL': Invalid base URL
    at st (url.js:15:10)
    at ut (url.js:22:19)
    at n.value (info.jsx:70:15)
    at u._renderValidatedComponentWithoutOwnerOrContext (ReactCompositeComponent.js:796:30)
    at u._renderValidatedComponent (ReactCompositeComponent.js:819:32)
    at u._updateRenderedComponent (ReactCompositeComponent.js:743:36)
    at u._performComponentUpdate (ReactCompositeComponent.js:721:10)
    at updateComponent (ReactCompositeComponent.js:642:12)
    at u.receiveComponent (ReactCompositeComponent.js:544:10)
    at Object.receiveComponent (ReactReconciler.js:122:22)
(anonymous) @ system.js:490
(anonymous) @ index.js:22
r @ system.js:175
(anonymous) @ system.js:487
(anonymous) @ actions.js:77
(anonymous) @ utils.js:177
(anonymous) @ bindActionCreators.js:3
(anonymous) @ wrap-actions.js:5
r @ system.js:175
(anonymous) @ system.js:487
(anonymous) @ index.js:11
r @ system.js:175
(anonymous) @ system.js:487
f @ download-url.js:35
Promise.then (async)
(anonymous) @ download-url.js:24
(anonymous) @ utils.js:177
(anonymous) @ bindActionCreators.js:3
m @ index.js:188
i @ spec-actions.js:22
Promise.then (async)
(anonymous) @ spec-actions.js:11
(anonymous) @ utils.js:177
(anonymous) @ bindActionCreators.js:3
Lr @ index.js:210
window.onload @ (index):40
load (async)
(anonymous) @ (index):38
```
_Swagger UI Authorize_
```java
url.js:15 Uncaught TypeError: Failed to construct 'URL': Invalid base URL
    at st (url.js:15:10)
    at ut (url.js:22:19)
    at n.value (info.jsx:70:15)
    at u._renderValidatedComponentWithoutOwnerOrContext (ReactCompositeComponent.js:796:30)
    at u._renderValidatedComponent (ReactCompositeComponent.js:819:32)
    at u._updateRenderedComponent (ReactCompositeComponent.js:743:36)
    at u._performComponentUpdate (ReactCompositeComponent.js:721:10)
    at updateComponent (ReactCompositeComponent.js:642:12)
    at u.receiveComponent (ReactCompositeComponent.js:544:10)
    at Object.receiveComponent (ReactReconciler.js:122:22)
```

### Steps to reproduce
Example OAS:
_YAML_
```yaml
info:
  license:
    name: Request Access Token (JWT)
    url: /authorization-code
```
_JSON_
```java
"info": {
  "license": {
    "name": "Request Access Token (JWT)",
    "url": "/authorization-code"
}
```


### Additional info:

Output of the commands:

- `Python 3.9.5`
- `Version: 2.10.0`
