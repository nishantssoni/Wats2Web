pre = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <script src="https://kit.fontawesome.com/391827d54c.js" crossorigin="anonymous"></script>
  <style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&display=swap');

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: 'Poppins', sans-serif;
}

body {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background: #ece5dd;
}

.background-green {
  position: absolute;
  top: 0;
  width: 100%;
  height: 20%;
  background-color: #075e54;
}

.main-container {
  position: relative;
  width: 1000px;
  max-width: 100%;
  height: calc(100vh - 40px);
  background: #fff;
  display: flex;
  box-shadow: 0px 1px 1px 0 rgba(0,0,0,0.5), 0px 2px 5px 0 rgba(0,0,0,0.6);
  border-radius: 10px;
  overflow: hidden;
}

.main-container .right-container {
  position: relative;
  width: 70%;
  height: 100%;
  flex: 70%;
  background: #e5ddd5;
  display: flex;
  flex-direction: column;
}

.chat-container {
  position:relative;
  width: 100%;
  height: calc(100vh - 60px);
  padding: 20px;
  overflow-y: auto;
  flex-grow: 1;
}

.message-box {
  position:relative;
  display: flex;
  width:100%;
  margin: 10px 0;
  align-items: flex-end;
}

.message-box p {
  max-width: 70%;
  padding: 10px 15px;
  background: #dcf8c6;
  border-radius: 10px;
  font-size: 0.95em;
  position: relative;
  word-wrap: break-word;
  white-space: pre-wrap;
}

.message-box.my-message p {
  background: #dcf8c6;
}

.message-box.friend-message p {
  background: #fff;
}

.message-box p span {
  display: block;
  margin-top: 5px;
  font-size: 0.75em;
  opacity: 0.6;
  text-align: right;
}

.my-message {
  justify-content: flex-end;
}

.friend-message {
  justify-content: flex-start;
}

.message-box.my-message p::before {
  content: '';
  position: absolute;
  top: 0;
  right: -8px;
  width: 20px;
  height: 20px;
  background: linear-gradient(135deg, #dcf8c6 50%, transparent 50%);
}

.message-box.friend-message p::before {
  content: '';
  position: absolute;
  top: 0;
  left: -8px;
  width: 20px;
  height: 20px;
  background: linear-gradient(225deg, #fff 50%, transparent 50%);
}

.message-box img {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  margin: 0 10px;
}

.message-box a {
  color: #065fd4;
  text-decoration: none;
  word-break: break-all;
}

  </style>
  <title>Whatsapp Clone</title>
</head>
<body>
 
    <div class="background-green"></div>

  <div class="main-container">
    <div class="right-container">
    <div class="chat-container">
'''

post = '''
</div>
 </div>
  </div>
</body>
</html>

<script>
  document.addEventListener("DOMContentLoaded", function() {
    const links = document.querySelectorAll(".message-box a");
    links.forEach(link => {
      if (link.textContent.length > 50) {
        link.textContent = link.textContent.substring(0, 47) + "...";
      }
    });
  });
</script>

'''

def my_msg(msg, author, time):
    return f'''
    <div class="message-box my-message">
      <p>{msg}<br><span>{author} - {time}</span></p>
    </div>'''

def my_frnd_msg(msg, author, time):
    return f'''
    <div class="message-box friend-message">
      <img src="https://via.placeholder.com/30" alt="friend">
      <p>{msg}<br><span>{author} - {time}</span></p>
    </div>'''
