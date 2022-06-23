clear

banner1 (){ 


echo "╭━━━━╮------------------------"
echo "┃This Script is  To Install and run Tools ┃"
echo "╰━┳━━-------------------------"
echo "  ┃"
echo "　◣ ◢　　　　　　◢◤"
echo "　▉▉▉　　　　　◢◤"
echo "　▉▉▉▃▃▃▃▃▃▉"
echo "　　◥▉▉▉▉▉▉▉▉"
echo "　　　▉▉▉▉▉▉▉▉"
echo "　　　▋ ▋ 　▋ ▋"
echo "　　　▋ ▋　 ▋ ▋"
echo "　　　▋ ▋ 　▋ ▋"

}

By1 (){

echo " ⊂_ヽ"
echo "　 ＼＼  Λ＿Λ"
echo "　　 ＼( 'ㅅ' )"
echo "　　　 >　⌒ヽ"
echo "　　　/ 　 へ＼"
echo "　　 /　　/　＼＼"
echo "　　 ﾚ　ノ　　 ヽ_つ"
echo "　　/　/"
echo "　 /　/|"              
echo "　(　(ヽ                  ═╬════════► by Pro For Termux"
echo "　|　|、＼"
echo "　| 丿 ＼ ⌒)"
echo "　| |　　) /"
echo " ノ )　　Lﾉ"

}


goodbye (){

echo "  _     _     _  "
echo "/  \   / \   / \ "
echo "( B ) ( y ) ( e )"
echo " \_/   \_/   \_/" 

}

echo ""

banner1


echo ""

echo "If YoU WoUld run Tools Write 'yes' else 'no' : "

read yesorno

if [ $yesorno = yes ];then


echo "===||:::::::::::::::>wait To Install===||:::::::::::::::>"

apt update && apt update

apt list --upgradable

pkg install python

pkg install python2

pip install V7xStyle

pip install --upgrade pip

pip install V7xStyle

pip3 install pyfiglet 

pip install --upgrade pip

pip install pyfiglet

echo "Installed Successufuly , Now The Tools open Automatiquely......"

clear


echo -e "===||:::::::::::::::::>Wait 10 seconds To run Tools<::::::::::::::::===)"

sleep 15

timeout 10 

python3 ProForTermux.py
exit

elif [ $yesorno = no ];then


echo "═╬════════►Bye Bye Good Luck═╬════════►"


By1


exit

else

echo ""

echo "(===||:::::::::::::::>Write yes or no(===||:::::::::::::::> "

echo ""

goodbye

echo ""

exit
fi
