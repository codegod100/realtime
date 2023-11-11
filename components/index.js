import Clock from './Clock.svelte';
import Input from './Input.svelte';
import Api from './Api.svelte';
import BigClock from './BigClock.svelte';
new BigClock({
    target: document.querySelector('#clock'),
});

new Input({
    target: document.querySelector('#input-component'),
});

new Api({
    target: document.querySelector('#api'),
})