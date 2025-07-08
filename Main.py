<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Nurseflix - 건강관리 시뮬레이터</title>
  <style>
    body { font-family: Arial, sans-serif; margin: 30px; }
    input, button { margin: 5px; padding: 8px; font-size: 16px; }
    #output { margin-top: 20px; white-space: pre-wrap; background: #f0f0f0; padding: 15px; }
  </style>
</head>
<body>
  <h2>🩺 Nurseflix - 개인 맞춤 간호 서비스</h2>

  <input id="name" placeholder="이름" />
  <input id="age" type="number" placeholder="나이" />
  <input id="condition" placeholder="건강 상태 (예: 임산부, 노인, 일반)" />
  <input id="sleep" type="number" placeholder="수면 시간 (시간)" />
  <input id="meals" type="number" placeholder="식사 여부 (1=했음, 0=안 했음)" />
  <input id="mood" placeholder="기분 (예: 좋음, 나쁨)" />
  <br>
  <button onclick="recommend()">간호 추천 보기</button>

  <div id="output"></div>

  <script>
    function recommend() {
      const name = document.getElementById("name").value;
      const age = parseInt(document.getElementById("age").value);
      const condition = document.getElementById("condition").value.toLowerCase();
      const sleep = parseInt(document.getElementById("sleep").value);
      const meals = parseInt(document.getElementById("meals").value);
      const mood = document.getElementById("mood").value;

      let result = `=== ${name}님의 맞춤 간호 추천 ===\n`;

      if (condition.includes("임산부"))
        result += "- 산후 회복, 정서 관리 제공\n";
      else if (condition.includes("노인") || age > 70)
        result += "- 낙상 예방, 정서 돌봄\n";
      else
        result += "- 일반 건강 상담 및 생활습관 케어\n";

      if (sleep < 6)
        result += "- 수면 부족: 수면 유도 오디오 제공\n";

      if (meals === 0)
        result += "- 식사 미흡: 맞춤 식단 관리 필요\n";

      result += `\n현재 기분: ${mood}`;

      document.getElementById("output").textContent = result;
    }
  </script>
</body>
</html>
