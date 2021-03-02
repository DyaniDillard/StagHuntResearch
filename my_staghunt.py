from pythonian import Pythonian
import socialSim.run_sim as sim
import logging

logger = logging.getLogger('StagHuntAgent')

class StagHuntAgent(Pythonian):

    name = "StagHuntAgent"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # TODO: lookup
        self.add_achieve(sim.my_run_sim, 'run_sim')


if __name__ == "__main__":
    logger.setLevel(logging.DEBUG)
    a = StagHuntAgent(host='localhost', port=9000, localPort=8950, debug=True)
    # AGENT = TestAgent.parse_command_line_args()

# (achieve :receiver StagHuntAgent :content (task :action (run_sim (2, 1, 3) 3)))
