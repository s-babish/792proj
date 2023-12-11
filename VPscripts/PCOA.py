#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 10:00:55 2023
PRINCIPLE COORDINATE ANALYSIS with 
MULTIVARIATE MEDIAN TOM-FOOLERY
@author: christian
"""
# Example usage:
# Define your distance matrix D here

import numpy as np

class pcoa(object):
    """
        Principle Coordinate Analysis
        Takes 2D-Array, eg.: 
        D = np.array([[0, 3, 4, 5], [3, 0, 6, 7], [4, 6, 0, 8], [5, 7, 8, 0]]) 
        Performs PCoA and Stores eigvals, eigvectors, Coords
    """
    def __init__(self, D):
        self.data = np.array(D)
        
        # pcoa calculation
        n = self.data.shape[0]
        H = np.eye(n) - np.ones((n, n)) / n
        B = -0.5 * H.dot(self.data ** 2).dot(H)
        
        eigvals, eigvecs = np.linalg.eigh(B)
        idx = np.argsort(eigvals)[::-1]
        
        self.eigvals = eigvals[idx]
        self.eigvecs = eigvecs[:, idx]
        
        self.coords = np.sqrt(np.diag(self.eigvals)).dot(self.eigvecs.T)
        
        self.sample_indices = self.length_coords()
        self.samples = self.coords.T
        
    def length_coords(self, ):
        '''
        Parameters: self
        ----------
        Returns Vector of Length self.coords
        -------
        '''
        n = [i for i in range(1, len(self.coords))]
        n.append(len(self.coords))
        return n
            
    def percentile_per_coords(self, default_percentile = 50 ):
        '''
        Parameters: self, default_percentile (the percentile used to calculate median
        is 50 by default)
        ----------
        default_percentile : TYPE, optional
            DESCRIPTION. The default is 50.
        Returns dictionary containing percentiles by index
        -------
        percentiles : TYPE
            DESCRIPTION.
        '''
        percentiles = {}
        for index, sample in iter(zip(self.sample_indices, self.coords)):
            percentiles.update({index: np.percentile(sample, default_percentile)})
        return percentiles


# %%

    

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
