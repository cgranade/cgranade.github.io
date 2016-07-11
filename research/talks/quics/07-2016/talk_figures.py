from __future__ import division
import qinfer as qi
import numpy as np

class SampleTimeHeuristic(qi.Heuristic):

    def __init__(self,
            updater, t_func,
            t_field=None, other_fields=None
        ):
        super(SampleTimeHeuristic, self).__init__(updater)
        self._t_func = t_func
        self._t_field = t_field
        self._other_fields = other_fields

    def __call__(self):
        n_exps = len(self._updater.data_record)
        t = self._t_func(1 + n_exps)
        dtype = self._updater.model.expparams_dtype

        if self._t_field is None:
            return np.array([t], dtype=dtype)
        else:
            eps = np.empty((1,), dtype=dtype)
            for field, value in self._other_fields.items():
                eps[field] = value
            eps[self._t_field] = t
            return eps

class UnknownT2Model(qi.Model):
    ## PROPERTIES ##
    
    @property
    def n_modelparams(self):
        return 2
    
    @property
    def modelparam_names(self):
        return [r'\omega', r'1 / T_2']
        
    @property
    def expparams_dtype(self):
        return 'float'
    
    @property
    def is_n_outcomes_constant(self):
        return True
    
    ## METHODS ##
    
    def are_models_valid(self, modelparams):
        return np.all(modelparams > 0, axis=1)
    
    def n_outcomes(self, expparams):
        """
        Returns an array of dtype ``uint`` describing the number of outcomes
        for each experiment specified by ``expparams``.
        
        :param numpy.ndarray expparams: Array of experimental parameters. This
            array must be of dtype agreeing with the ``expparams_dtype``
            property.
        """
        return 2
    
    def likelihood(self, outcomes, modelparams, expparams):
        # By calling the superclass implementation, we can consolidate
        # call counting there.
        super(UnknownT2Model, self).likelihood(
            outcomes, modelparams, expparams
        )

        # Possibly add a second axis to modelparams.
        if len(modelparams.shape) == 1:
            modelparams = modelparams[..., np.newaxis]
            
        t = expparams
        w, gamma2 = modelparams.T[..., np.newaxis]
        
        # Allocating first serves to make sure that a shape mismatch later
        # will cause an error.
        pr0 = np.zeros((modelparams.shape[0], expparams.shape[0]))
        viz = np.exp(-t * gamma2)
        pr0[:, :] = np.cos(t * w / 2) ** 2
        pr0[:, :] = viz * pr0 + (1 - viz) / 2
        
        # Now we concatenate over outcomes.
        return qi.Model.pr0_to_likelihood_array(outcomes, pr0)
