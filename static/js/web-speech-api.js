var messages = {
  "start": {
    msg: 'Click on the microphone icon and start answering.',
    class: 'alert-success'},
  "speak_now": {
    msg: 'Speak now.',
    class: 'alert-success'},
  "no_speech": {
    msg: 'No speech was detected. Click on the microphone icon to try again.',
    class: 'alert-warning'},
  "no_microphone": {
    msg: 'No microphone was found. Ensure that a microphone is installed and that <a href="//support.google.com/chrome/answer/2693767" target="_blank">microphone settings</a> are configured correctly.',
    class: 'alert-danger'},
  "allow": {
    msg: 'Click the "Allow" button above to enable your microphone.',
    class: 'alert-warning'},
  "denied": {
    msg: 'Permission to use microphone was denied.',
    class: 'alert-danger'},
  "blocked": {
    msg: 'Permission to use microphone is blocked. To change, go to chrome://settings/content/microphone',
    class: 'alert-danger'},
  "upgrade": {
    msg: 'Interactive reading is not supported by this browser. It is only supported by <a href="//www.google.com/chrome">Chrome</a> version 25 or later on desktop and Android mobile.',
    class: 'alert-danger'},
  "stop": {
      msg: 'Click on the microphone icon to try again',
      class: 'alert-success'},
  // "copy": {
  //   msg: 'Content copy to clipboard successfully.',
  //   class: 'alert-success'},
}

var final_transcript = '';
var recognizing = false;
var ignore_onend;
var start_timestamp;
var recognition;
var answered = false;

$( document ).ready(function() {
  for (var i = 0; i < langs.length; i++) {
    select_language.options[i] = new Option(langs[i][0], i);
  }
  select_language.selectedIndex = lang_idx;
  updateCountry();
  select_dialect.selectedIndex = dial_idx;
  
  if (!('webkitSpeechRecognition' in window)) {
    upgrade();
  } else {
    showInfo('start');
    start_button.style.display = 'inline-block';
    recognition = new webkitSpeechRecognition() || new SpeechRecognition();;
    recognition.continuous = true;
    recognition.interimResults = true;

    /*once question was asked, recognition auto starts immediately*/
    var prompt_ques_link = document.getElementById('promptquestion');
    prompt_ques_link.onended = function(){                          
      initialize();
    };

    recognition.onstart = function() {
      recognizing = true;
      showInfo('speak_now');
      start_img.src = 'static/images/mic-animation.gif';
    };

    recognition.onerror = function(event) {
      if (event.error == 'no-speech') {
        start_img.src = 'static/images/mic.gif';
        showInfo('no_speech');
        tip_audio = new Audio('static/audio/click_microphone_tip.wav');
        tip_audio.play();
        ignore_onend = true;
      }
      if (event.error == 'audio-capture') {
        start_img.src = 'static/images/mic.gif';
        showInfo('no_microphone');
        ignore_onend = true;
      }
      if (event.error == 'not-allowed') {
        if (event.timeStamp - start_timestamp < 100) {
          showInfo('blocked');
        } else {
          showInfo('denied');
        }
        ignore_onend = true;
      }
    };

    recognition.onend = function () {     
      recognizing = false;
      if (ignore_onend) {
        return;
      }
      start_img.src = 'static/images/mic.gif';
      if (!final_transcript) {
        showInfo('start');
        return;
      }
      showInfo('stop');
      if (window.getSelection) {
        window.getSelection().removeAllRanges();
        var range = document.createRange();
        range.selectNode(document.getElementById('final_span'));
        window.getSelection().addRange(range);
      }

      if (final_transcript) {
        answer_audio = new Audio(prompt_ans);
        answer_audio.play();
        answer_audio.onended = function(){                          
            redirectHandler(url);
        };
      }


    };

    recognition.addEventListener('speechend', function() {
        //   timeoutHandle = window.setTimeout(function () {
        //   if (recognizing) {
        //     recognition.stop();
        //     sound_effect = new Audio('static/audio/floop2_x.wav');
        //     sound_effect.play();
        //     return;
        //   }
        // }, 7.0*1000);
      var answer_data = [
        {"question": question_id},
        {"result": answered}
      ];
      $.ajax({
        type: "POST",
        url: "process_answer",
        data: JSON.stringify(answer_data),
        contentType: "application/json",
        dataType: 'json'
      });
      
      if (answered) {
        sound_effect = new Audio('static/audio/chime_up.wav');
        sound_effect.play();         
      }
      else {
          sound_effect = new Audio('static/audio/floop2_x.wav');
          sound_effect.play();          
        }

    });
       
    recognition.onresult = function (event) {         
      var interim_transcript = '';

      for (var i = event.resultIndex; i < event.results.length; ++i) {
        
        if (event.results[i].isFinal) {
          final_transcript += event.results[i][0].transcript;
        } else {
          interim_transcript += event.results[i][0].transcript;
        }
      }
      var temp = '';
      for (var i = 0; i < keywords.length; i++){
        if (final_transcript.includes(keywords[i])){
          temp += keywords[i] + ';';
        }
      }
      if (temp) {
        answered = true;
        final_transcript = temp;
      }

      final_span.innerHTML = linebreak(final_transcript);
      interim_span.innerHTML = linebreak(interim_transcript);

    };
  }
});

 function redirectHandler(redirect_url) {
  window.location.href = redirect_url;
}

function updateCountry() {
  for (var i = select_dialect.options.length - 1; i >= 0; i--) {
    select_dialect.remove(i);
  }
  var list = langs[select_language.selectedIndex];
  for (var i = 1; i < list.length; i++) {
    select_dialect.options.add(new Option(list[i][1], list[i][0]));
  }
  select_dialect.style.visibility = list[1].length == 1 ? 'hidden' : 'visible';
}


function upgrade() {
  start_button.style.visibility = 'hidden';
  showInfo('upgrade');
}

var two_line = /\n\n/g;
var one_line = /\n/g;
function linebreak(s) {
  return s.replace(two_line, '<p></p>').replace(one_line, '<br>');
}

var first_char = /\S/;
function capitalize(s) {
  return s.replace(first_char, function(m) { return m.toUpperCase(); });
}

// $("#copy_button").click(function () {
//   if (recognizing) {
//     recognizing = false;
//     recognition.stop();
//   }
//   setTimeout(copyToClipboard, 500);
  
// });

// function copyToClipboard() {
//   if (document.selection) { 
//       var range = document.body.createTextRange();
//       range.moveToElementText(document.getElementById('results'));
//       range.select().createTextRange();
//       document.execCommand("copy"); 
  
//   } else if (window.getSelection) {
//       var range = document.createRange();
//        range.selectNode(document.getElementById('results'));
//        window.getSelection().addRange(range);
//        document.execCommand("copy");
//   }
//   showInfo('copy');
// }

$("#start_button").click(function () {
  if (recognizing) {
    recognition.stop();
    return;
  }
  initialize();
});

$("#select_language").change(function () {
  updateCountry();
});

function initialize() {
  final_transcript = '';
  recognition.lang = select_dialect.value;
  recognition.start();
  ignore_onend = false;
  final_span.innerHTML = '';
  interim_span.innerHTML = '';
  start_img.src = 'static/images/mic-slash.gif';
  showInfo('allow');
  start_timestamp = event.timeStamp;
}


function showInfo(s) {
  if (s) {
    var message = messages[s];
    $("#info").html(message.msg);
    $("#info").removeClass();
    $("#info").addClass('alert');
    $("#info").addClass(message.class);
  } else {
    $("#info").removeClass();
    $("#info").addClass('d-none');
  }
}