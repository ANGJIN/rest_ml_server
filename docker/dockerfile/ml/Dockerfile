FROM tensorflow/tensorflow:2.3.0-jupyter

WORKDIR /tf/notebooks

COPY ./ml .

RUN mv ./jupyter_notebook_config.py /root/.jupyter/jupyter_notebook_config.py

EXPOSE 8888

CMD [ "jupyter", "notebook" ]
