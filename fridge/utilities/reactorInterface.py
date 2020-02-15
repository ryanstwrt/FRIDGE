class reactorInterface(object):
    """The reactor interface is an easy way to explore different parameters within a specific reactor.
    This includes multiple methods to query the database."""
    def __init__(self, reactor):
        self.rx = reactor
        self.rx_name = self.rx.name.split('/')[-1]
        try:
            self.assemblies = {}
            for step in self.rx['{}_BU'.format(self.rx_name)].keys():
                self.assemblies[step] = self.rx['{}_BU'.format(self.rx_name)][step]['assemblies']
        except KeyError:
            print("Warning: Core {} does not have a burnup core. No assemblies are present".format(rx_name))
        
    def get_assembly_average(self, step, param):
        """Get the average parameter of an assembly based on the time step"""
        assem_tot = 0
        for num, assem in enumerate(self.assemblies[step].values()):
            assem_val = assem[param][0]
            assem_tot += assem_val
        return assem_tot / num
    
    def get_assembly_min(self, step, param):
        """Get the max parameter of an assembly based on the time step"""
        assem_min = 1E100
        for name, assem in self.assemblies[step].items():
            if assem[param][0] < assem_min:
                assem_min = assem[param][0]
                assem_name = name
        return (assem_name, assem_min)

    def get_assembly_max(self, step, param):
        """Get the max parameter of an assembly based on the time step"""
        assem_min = 0.0
        for name, assem in self.assemblies[step].items():
            if assem[param][0] > assem_min:
                assem_min = assem[param][0]
                assem_name = name
        return (assem_name, assem_min)
    
    def get_peak_to_average(self, step, param):
        avg = self.get_assembly_average(step, param)
        peak_assem, peak_val = self.get_assembly_max(step, param)
        return (peak_assem, peak_val / avg)
    
    def get_assem_to_avg(self, step, param, assem):
        avg = self.get_assembly_average(step, param)
        return self.assemblies[step][assem] / avg
        
