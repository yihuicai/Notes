# 	React.JS Chap2: Component Class

```react
class MyComponentClass extends React.Component
{ // everything in between these curly-braces is instructions for how to build components

  render() {
    return <h1>Hello world</h1>;
  }
}
```

This class declaration results in a new component class, in this case named `MyComponentClass`.`MyComponentClass` has one method, named `render`. This all happens via standard JavaScript class syntax.

You *haven't* learned how these instructions actually work to make components! When you make a component by using the expression `<MyComponentClass />`, what do these instructions do?

Whenever you make a component, that component *inherits* all of the methods of its component class. `MyComponentClass` has one method: `MyComponentClass.render()`. Therefore, `<MyComponentClass />` also has a method named `render`.

You could make a million different `<MyComponentClass />` instances, and each one would inherit this same exact `render` method.

This lesson's final exercise is to *render* your component. In order to render a component, that component needs to have a method named `render`. Your component has this! It *inherited* a method named `render` from `MyComponentClass`.

Since your component has a render method, all that's left to do is call it. This happens in a slightly unusual way.

To call a component's `render` method, you pass that component to `ReactDOM.render()`. Notice your component, being passed as `ReactDOM.render()`'s first argument:

```react
ReactDOM.render(
  <MyComponentClass />,
  document.getElementById('app')
);
```

`ReactDOM.render()` will tell `<MyComponentClass />` to call *its* render method.

`<MyComponentClass />` will call its render method, which will return the JSX element `<h1>Hello world</h1>`. `ReactDOM.render()` will then take that resulting JSX element, and add it to the virtual DOM. This will make "Hello world" appear on the screen.

### Use `this` in function

Render functions often contain event listeners. Here's an example of an event listener in a render function:

```jsx
render() {
  return (
    <div onHover={myFunc}>
    </div>
  );
}
```

Recall that an event *handler* is a function that gets called in response to an event. In the above example, the event handler is `myFunc()`.

In React, you define event handlers as *methods* on a component class. Like this:

```react
class MyClass extends React.Component {
  myFunc() {
    alert('Stop it.  Stop hovering.');
  }

  render() {
    return (
      <div onHover={this.myFunc}>
      </div>;
    );
  }
}
```

Notice that the component class has two methods:`.myFunc()` and `.render()`. `.myFunc()` is being used as an *event handler*. `.myFunc()` will be called any time that a user hovers over the rendered `<div></div>`.

------

### Require a file(Import)

When you use React.js, every JavaScript file in your application is invisible to every other JavaScript file by default. **ProfilePage.js** and **NavBar.js** can't see each other.

This is a problem!

On line 9, you just added an instance of the `NavBar`component class. But since you're in **ProfilePage.js**, JavaScript has no idea what `NavBar` means.

If you want to use a variable that's declared in a different file, such as `NavBar`, then you have to *import* the variable that you want. To import a variable, you can use an `import` statement:

```react
import { NavBar } from './NavBar.js';
```

We've used `import` before, but not like this! Notice the differences between the above line of code and this familiar line:

```react
import React from 'react';
```

The first important difference is the curly braces around `NavBar`. We'll get to those soon!

The second important difference involves the contents of the string at the end of the statement:`'react'` vs `'./NavBar.js'`.

If you use an `import` statement, and the string at the end begins with either a dot or a slash, then `import` will treat that string as a *filepath*. `import`will follow that filepath, and import the file that it finds.

If your filepath doesn't have a file extension, then ".js" is assumed. So the above example could be shortened:

```react
import { NavBar } from './NavBar';
```

**One final, important note:**
None of this behavior is specific to React! [Module systems](http://eloquentjavascript.net/10_modules.html) of independent, importable files are a very popular way to organize code. [React's specific module system comes from ES6](https://hacks.mozilla.org/2015/08/es6-in-depth-modules/). More on all of that later.

### Export

Alright! You've learned how to use `import` to grab a variable from a file *other than* the file that is currently executing.

When you import a variable from a file that is not the current file, then an `import` statement isn't quite enough. You also need an `export` statement, written in the *other* file, exporting the variable that you hope to grab.

`export` comes from [ES6's module system,](http://exploringjs.com/es6/ch_modules.html) just like `import` does. `export` and `import` are meant to be used together, and you rarely see one without the other.

There are a few different ways to use `export`. In this course, we will be using a style called "named exports." Here's how named exports works:

In one file, place the keyword `export` immediately before something that you want to export. That something can be any top-level `var`, `let`, `const`, `function`, or `class`:

```react
// Manifestos.js:

export const faveManifestos = {
  futurist: 'http://bit.ly/1lKuB2I',
  SCUM:     'http://bit.ly/1xWjvYc',
  cyborg:   'http://bit.ly/16sbeoI'
};
```

You can export multiple things from the same file:

```react
// Manifestos.js:

export const faveManifestos = {
  futurist: 'http://bit.ly/1lKuB2I',
  SCUM:     'http://bit.ly/1xWjvYc',
  cyborg:   'http://bit.ly/16sbeoI'
};

export const alsoRan = 'TimeCube';
```

In a different file, `import` the name of the `var`, `let`, `const`, `function`, or `class` from the first file:

```react
// App.js:

// Import faveManifestos and alsoRan from ./Manifestos.js:
import { faveManifestos, alsoRan } from './Manifestos';

// Use faveManifestos:
console.log(`A Cyborg Manifesto:  ${faveManifestos.cyborg}`);
```

This style of importing and exporting in JavaScript is known as "named exports." When you use named exports, you always need to wrap your imported names in curly braces, such as `import { faveManifestos, alsoRan } from './Manifestos';`.

You can read more about named exports, and about JavaScript's module system in general, [here](http://exploringjs.com/es6/ch_modules.html).

------

### Passing value to React Component by `props`

How? By giving that component an *attribute:*

```jsx
<MyComponent foo="bar" />
```

Let's say that you want to pass a component the message, `"This is some top secret info."`. Here's how you could do it:

```jsx
<Example message="This is some top secret info." />
```

As you can see, to pass information to a component, you need a *name* for the information that you want to pass.

In the above example, we used the name `message`. You can use any name you want.

If you want to pass information that isn't a string, then wrap that information in curly braces. Here's how you would pass an array:

```jsx
<Greeting myInfo={["top", "secret", "lol"]} />
```

In this next example, we pass several pieces of information to `<Greeting />`. The values that aren't strings are wrapped in curly braces:

```jsx
<Greeting name="Frarthur" town="Flundon" age={2} haunted={false} />
```

------

### Pass props From Component to Component

In the first file, we define the way to render the props in the JSX of render function, and export it for other Components in other files to use.

```react
import React from 'react';

export class Greeting extends React.Component {
  render() {
    return <h1>Hi there, {this.props.name}!</h1>;
  }
}
```

```react
import React from 'react';
import ReactDOM from 'react-dom';
import {Greeting} from './Greeting.js'
class App extends React.Component {
  render() {
    return (
      <div>
        <h1>
          Hullo and, "Welcome to The Newzz," "On Line!"
        </h1>
        <Greeting name="Alan"/>
        <article>
          Latest newzz:  where is my phone?
        </article>
      </div>
    );
  }
}

ReactDOM.render(
  <App />, 
  document.getElementById('app')
);
```

In the second file, we add the Component instance into the other Component, define the props in the DOM rendering part.

------

You can do more with `props` than just display them. You can also use `props` to make decisions.

In the code editor, look at the `Welcome` component class.

You can tell from `this.props.name` on line 5 that `Welcome` expects to receive a piece of information called *name*. However, `Welcome` never renders this piece of information! Instead, it uses the information to make a decision.

`<Welcome />` instances will render the text `WELCOME "2" MY WEB SITE BABYYY!!!!!`, unless the user is Mozart, in which case they will render the more respectful
`hello sir it is truly great to meet you`
`here on the web`.

The passed-in *name* is not displayed in either case! The name is used to *decide* what will be displayed. This is a common technique.

```react
import React from 'react';
import ReactDOM from 'react-dom';

export class Greeting extends React.Component {
  render() {
  	if (this.props.signedIn == false) {
  	  return <h1>GO AWAY</h1>;
  	} else {
  	  return <h1>Hi there, {this.props.name}!</h1>;
  	}
  }
}
```



```react
import React from 'react';
import ReactDOM from 'react-dom';
import { Greeting } from './Greeting';

class App extends React.Component {
  render() {
    return (
      <div>
        <h1>
          Hullo and, "Welcome to The Newzz," "On Line!"
        </h1>
        <Greeting name="Alison" signedIn={true}/>
        <article>
          Latest:  where is my phone?
        </article>
      </div>
    );
  }
}

ReactDOM.render(
  <App />, 
  document.getElementById('app')
);
```



------

### Event Handler in React

Let's talk about naming things.

When you pass an *event handler* as a prop, as you just did, there are two names that you have to choose.

Both naming choices occur in the *parent* component class - that is, in the component class that defines the event handler and passes it.

The first name that you have to choose is the name of the event handler itself.

Look at **Talker.js**, lines 6 through 12. This is our event handler. We chose to name it `talk`.

The second name that you have to choose is the name of the prop that you will use to *pass* the event handler. This is the same thing as your attribute name.

For our prop name, we also chose `talk`, as shown on line 15:

```
return <Button talk={this.talk} />;
```

These two names can be whatever you want. However, there is a naming convention that they often follow. You don't have to follow this convention, but you should understand it when you see it.

Here's how the naming convention works: first, think about what *type of event* you are listening for. In our example, the event type was "click."

If you are listening for a "click" event, then you name your *event handler* `handleClick`. If you are listening for a "keyPress" event, then you name your event handler `handleKeyPress`:

```react
class MyClass extends React.Component {
  handleHover() {
    alert('I am an event handler.');
    alert('I will be called in response to "hover" events.');
  }
}
```

Your prop name should be the word `on`, plus your event type. If you are listening for a "click" event, then you name your prop `onClick`. If you are listening for a "keyPress" event, then you name your prop `onKeyPress`:

```react
class MyClass extends React.Component {
  handleHover() {
    alert('I am an event handler.');
    alert('I will listen for a "hover" event.');
  }

  render() {
    return <Child onHover={this.handleHover} />;
  }
}
```

------

```react
//Talker.js
import React from 'react';
import ReactDOM from 'react-dom';
import { Button } from './Button';

class Talker extends React.Component {
  handleClick() {
    let speech = '';
    for (let i = 0; i < 10000; i++) {
      speech += 'blah ';
    }
    alert(speech);
  }
  
  render() {
    return <Button onClick={this.handleClick} />;
  }
}

ReactDOM.render(
  <Talker />,
  document.getElementById('app')
);
```

 

```react
//Button.js
import React from 'react';

export class Button extends React.Component {
  render() {
    return (
      <button onClick={this.props.onClick}>
        Click me!
      </button>
    );
  }
}
```

One major source of confusion is the fact that names like `onClick` have special meaning, but only if they're used on HTML-like elements.

Look at **Button.js**. When you give a `<button></button>` an attribute named `onClick`, then the name `onClick` has special meaning. As you've learned, this special `onClick` attribute creates an *event listener*, listening for clicks on the `<button></button>`:

```react
// Button.js

// The attribute name onClick
// creates an event listner:
<button onClick={this.props.onClick}>
  Click me!
</button>
```

Now look at **Talker.js**. Here, when you give `<Button />` an attribute named `onClick`, then the name `onClick` doesn't do anything special. The name `onClick` does *not* create an event listener when used on `<Button />` - it's just an arbitrary attribute name:

```react
// Talker.js

// The attribute name onClick
// is just a normal attribute name:
<Button onClick={this.handleClick} />
```

The reason for this is that in `<Button />` is not an HTML-like JSX element; it's a *component instance*.

Names like `onClick` only create event listeners if they're used on HTML-like JSX elements. Otherwise, they're just ordinary prop names.

------

### The `props.children`

When Component instance is called and props are define, they have wrapped other component instances also. The `props.children` can manipulate the children elements of the wrapped elements.

```react
//App.js

import React from 'react';
import ReactDOM from 'react-dom';
import { List } from './List';

class App extends React.Component {
  render() {
    return (
      <div>
        <List type='Living Musician'>
          <li>Sachiko M</li>
          <li>Harvey Sid Fisher</li>
        </List>
        <List type='Living Cat Musician'>
          <li>Nora the Piano Cat</li>
        </List>
      </div>
    );
  }
}

ReactDOM.render(
  <App />, 
  document.getElementById('app')
);
```



```react
//List.js

import React from 'react';

export class List extends React.Component {
  render() {
    let titleText = `Favorite ${this.props.type}`;
    if (this.props.children instanceof Array) {
    	titleText += 's';
    }
    return (
      <div>
        <h1>{titleText}</h1>
        <ul>{this.props.children}</ul>
      </div>
    );
  }
}
```

BONUS: Each `<List><List />` instance is passed a singular title: "Living Musician" and "Living Cat Musician," respectively. Somehow, each `<List><List />` counts its list-items and automatically adds an "s" to the end of its title if the count is greater than one. We could add a second piano cat, and the second list title would automatically pluralize.

See if you can figure out how the instances of the `List` component class are automatically pluralizing their titles!

### DefaultProps

Take a look at the `Button` component class.

Notice that on line 8, `Button` expects to receive a prop named `text`. The received `text` will be displayed inside of a `<button></button>` element.

What if nobody passes any `text` to `Button`?

If nobody passes any `text` to `Button`, then `Button`'s display will be blank. It would be better if `Button` could display a default message instead.

You can make this happen by giving your component class a property named `defaultProps`:

```react
class Example extends React.Component {
  render() {
    return <h1>{this.props.text}</h1>;
  }
}

Example.defaultProps;
```

The `defaultProps` property should be equal to an object:

```react
class Example extends React.Component {
  render() {
    return <h1>{this.props.text}</h1>;
  }
}

// Set defaultProps equal to an object:
Example.defaultProps = {};
```

Inside of this object, write properties for any default `props` that you'd like to set:

```react
class Example extends React.Component {
  render() {
    return <h1>{this.props.text}</h1>;
  }
}

Example.defaultProps = { text: 'yo' };
```

If an `<Example />` doesn't get passed any text, then it will display "yo."

If an `<Example />` *does* get passed some text, then it will display that passed-in text.