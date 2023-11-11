<script>
  let date = new Date();
  setInterval(() => {
    date = new Date();
  }, 1000);
</script>

The time is {date.toLocaleTimeString()}
