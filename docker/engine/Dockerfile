FROM scoringengine/base

COPY bin/engine /app/bin/engine

COPY scoring_engine /app/scoring_engine
RUN pip install -e .
RUN chmod +x /app/scoring_engine/checks/bin/rdp_check


CMD ["./wait-for-container.sh", "bootstrap", "/app/bin/engine"]
