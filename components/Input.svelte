<script>
  let text = "";
  import Clock from "./Clock.svelte";
</script>

<input
  class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
  type="text"
  placeholder="This is a svelte component"
  bind:value={text}
/>

<button
  on:click={() => alert(text)}
  class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
  >Submit</button
>
<div>{text}</div>
