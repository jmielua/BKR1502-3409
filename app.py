{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app '__main__' (lazy loading)\n",
      " * Environment: production\n",
      "\u001b[31m   WARNING: This is a development server. Do not use it in a production deployment.\u001b[0m\n",
      "\u001b[2m   Use a production WSGI server instead.\u001b[0m\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Running on http://127.0.0.1:1111/ (Press CTRL+C to quit)\n",
      "127.0.0.1 - - [15/Feb/2022 11:12:38] \"GET / HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.01 0.01 0.02\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2022-02-15 11:12:55.558370: I tensorflow/core/platform/cpu_feature_guard.cc:151] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 FMA\n",
      "To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.\n",
      "127.0.0.1 - - [15/Feb/2022 11:12:56] \"POST / HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[0.40683046]]\n"
     ]
    }
   ],
   "source": [
    "from flask import Flask\n",
    "app = Flask(__name__)\n",
    "\n",
    "\n",
    "from flask import request, render_template\n",
    "from keras.models import load_model\n",
    "\n",
    "@app.route(\"/\", methods=[\"GET\", \"POST\"])\n",
    "def index():\n",
    "    if request.method==\"POST\":\n",
    "        NPTA = request.form.get(\"NPTA\")\n",
    "        TLTA = request.form.get(\"TLTA\")\n",
    "        WCTA = request.form.get(\"WCTA\")\n",
    "        print(NPTA, TLTA, WCTA)\n",
    "        model = load_model(\"/Users/jmielua/Desktop/UNI Studying Materials/Y3S1/BC3409 AI in Finance/Sem 5/Cloud Heroku/BKRNN\")\n",
    "        pred = model.predict([[float(NPTA), float(TLTA), float(WCTA)]])\n",
    "        print(pred)\n",
    "        return(render_template(\"index.html\", result=\"1\"))\n",
    "    else:\n",
    "        return(render_template(\"index.html\", result=\"2\"))\n",
    "    \n",
    "if __name__ == \"__main__\":\n",
    "    app.run(host = \"127.0.0.1\", port=1111)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "interpreter": {
   "hash": "40d3a090f54c6569ab1632332b64b2c03c39dcf918b08424e98f38b5ae0af88f"
  },
  "kernelspec": {
   "display_name": "Python 3.7.6 ('base')",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
